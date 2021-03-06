#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <ctime>
#include <stdint.h>

extern "C"
{
#include <libavcodec/avcodec.h>
#include <libavformat/avformat.h>
#include <libswscale/swscale.h>
#include <libavutil/motion_vector.h>
}

#include <string>
#include <algorithm>
#include <vector>
#include <stdexcept>


using namespace std;   // bad c++ practice but meh

AVFormatContext* format_context;
AVStream* video_stream;
AVFrame* frame_container;
int video_stream_index;
const char *VIDEO_PATH;


/*
 * Initialize ffmpeg connection
 *   - open up input file and video streams into format_context
 *   - get primary video stream into video_stream
 *   - allocate an empty container for frame_container
 */
void initialize_ffmpeg() {
    // Initializes libavformat and registers all the muxers, demuxers and protocols
    av_register_all();

    // set up empty container frame/context to parse into
    frame_container = av_frame_alloc();                      // https://www.ffmpeg.org/doxygen/2.7/structAVFrame.html
    format_context = avformat_alloc_context();     // https://ffmpeg.org/doxygen/2.7/structAVFormatContext.html
    video_stream_index = -1;

    int e = 0;
    // try to open input file
    if ((e = avformat_open_input(&format_context, VIDEO_PATH, NULL, NULL)) != 0)
      throw std::runtime_error("Couldn't open file!");

    // verify that input is video stream
    if ((e = avformat_find_stream_info(format_context, NULL)) < 0)
          throw std::runtime_error("Couldn't find stream info!");

    for (int i = 0; i < format_context->nb_streams; i++) {
	AVCodecContext *codec = format_context->streams[i]->codec;

	// skip to very start of video stream to grab metadata
	if (codec->codec_type == AVMEDIA_TYPE_VIDEO && video_stream_index < 0) {
	    AVCodec *codec_id = avcodec_find_decoder(codec->codec_id);
	    AVDictionary *operations = NULL;
	    av_dict_set(&operations, "flags2", "+export_mvs", 0);

	    if (avcodec_open2(codec, codec_id, &operations) < 0 || !codec_id)
		throw std::runtime_error("Couldn't open video codec!");

	    video_stream_index = i;                          // remember index where video stream starts
	    video_stream = format_context->streams[i];     // remember this stream as primary video stream

	    break;
	}
    }

    if (video_stream_index == -1)
    	throw std::runtime_error("ffmpeg failed to initialize -- video stream info not found!");
}


/*
 * Given a packet, decode the video frame in packet->data to 
 *   our empty frame container
 */
bool decode_packet_into_frame(AVPacket *packet) {
    av_frame_unref(frame_container);            // reset frame fields

    int got_frame = 0;

    // try to decode video frame into the frame container
    int ret_val = avcodec_decode_video2(video_stream->codec, frame_container, &got_frame, packet);

    // ret_val is neg if error, else num bytes used, else 0 if frame couldn't be decompressed
    if (ret_val < 0)
	return false;

    packet->data += ret_val;
    packet->size -= ret_val;
    return got_frame > 0;
}


/*
 * Loop through frames until you get to one you can decode, then read that 
 *  frame into a packet and decode it into our frame_container
 */
bool read_next_packet() {
    static bool initialized = false;
    static AVPacket packet;

    // keep reading in packets until you get a full video frame
    while (true) {
	if (initialized) {
	    // if you've read a frame into the packet, decode it into the frame_container
	    if (decode_packet_into_frame(&packet)) {
                return true;
	    // if packet decoding broke, start over from the top
	    } else {
		av_free_packet(&packet);
		initialized = false;
		continue;
	    }
	}
	// if uninitialized, try to read a frame into the packet 
	int ret = av_read_frame(format_context, &packet);
	// if reading it didn't work return false TODO STRUCTURE DIFFERENTLY?
	if (ret < 0)
	  return false;
	// if we're somehow at the wrong index, start over
	if (packet.stream_index != video_stream_index) {
	    av_free_packet(&packet);
	    continue;
	}
	// otherwise set initialized to true and copy the packet
	initialized = true;
    }
}    
    
/*
 *  Read the next frame into frame_container, then pull out motion vectors
 */
bool read_next_vectors(int64_t &timestamp, char &frame_type, vector<AVMotionVector> &vectors) {
    if (!read_next_packet()) 
      return false;

    frame_type = av_get_picture_type_char(frame_container->pict_type);           // get frame type ("I", "P", "B", etc.) from
                                                                                 // whatever's in global frame container 
                                                                                 // (that should be the current frame)
    // search frame for valid timestamp, if none exists, increment current timestamp
    if (frame_container->pkt_pts != AV_NOPTS_VALUE) {
	timestamp = frame_container->pkt_pts;
    } else if (frame_container->pkt_dts != AV_NOPTS_VALUE) {
	timestamp = frame_container->pkt_dts;
    } else {
	timestamp = timestamp + 1;
    }
    
    AVFrameSideData* side_data = av_frame_get_side_data(frame_container, AV_FRAME_DATA_MOTION_VECTORS);
    if (side_data != NULL) {
	AVMotionVector* motion_vecs = (AVMotionVector*)side_data->data;
	int num_vecs = side_data->size / sizeof(AVMotionVector);
	vectors = vector<AVMotionVector>(motion_vecs, motion_vecs + num_vecs);
    } else {
	vectors = vector<AVMotionVector>();
    }

    return true;
} 


/*
 * Print all the vectors in a frame as a csv
 *   format: 
 *           #HEADER
 *           x,y,dx,dy
 */
void print_vectors(int frame_i, int64_t timestamp, char frame_type, vector<AVMotionVector>& vectors) {
    printf("#ts=%ld,frame_i=%d,frame_type=%c,shape=%zux4\n", timestamp, frame_i, frame_type, vectors.size());
    int dx, dy;
    for (int i = 0; i < vectors.size(); i++) {
	AVMotionVector& v = vectors[i];
	dx = v.dst_x - v.src_x;
	dy = v.dst_y - v.src_y;
	printf("%d,%d,%d,%d\n", v.dst_x, v.dst_y, dx, dy);
    }
}



int main(int argc, const char* argv[]) {
    // get arg path
    VIDEO_PATH = argv[1];
    initialize_ffmpeg();

    int64_t timestamp = -1;
    int64_t prev_timestamp = -1;
    char frame_type;
    vector<AVMotionVector> vectors;

    for (int frame_i = 1; read_next_vectors(timestamp, frame_type, vectors); frame_i++) {
	if (timestamp <= prev_timestamp && prev_timestamp != -1) {
	    fprintf(stderr, "frame %d skipped -- timestamp: %d, prev timestamp: %d\n", int(frame_i), int(timestamp), int(prev_timestamp));
	    continue;
	}
	
	print_vectors(frame_i, timestamp, frame_type, vectors);

	prev_timestamp = timestamp;

    }

}










