#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <ctime>
#include <stdint.h>
#include <string>
#include <algorithm>
#include <vector>
#include <stdexcept>

extern "C"
{
#include <libavcodec/avcodec.h>
#include <libavformat/avformat.h>
#include <libswscale/swscale.h>
#include <libavutil/motion_vector.h>
}





AVFormatContext* format_context;
AVStream* video_stream;
size_t frame_width;
size_t frame_height;
AVFrame* frame;
int video_stream_index;


void initialize_ffmpeg(char *video_path) {
    // Initializes libavformat and registers all the muxers, demuxers and protocols
    av_register_all();

    // set up empty container frame/context to parse into
    frame = av_frame_alloc();                      // https://www.ffmpeg.org/doxygen/2.7/structAVFrame.html
    format_context = avformat_alloc_context();     // https://ffmpeg.org/doxygen/2.7/structAVFormatContext.html
    video_stream_index = -1;

    // try to open input file
    if ((e = avformat_open_input(&format_context, video_path, NULL, NULL)) != 0)
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
	    frame_width = codec->width;                      // get frame width & height
	    frame_height = codec->height;

	    break;
	}
    }

    if (video_stream_index == -1)
	throw std::runtime_error("ffmpeg failed to initialize -- video stream info not found!");
}




void read_frame(int64_t& num_vectors, char& frame_type, vector<AVMotionVector>& vectors) {
    // read data packets
    static bool initialized = false;
    static AVPacket packet;
    static AVPacket packet_cp;

    // keep reading in packets until you get a full video frame
    while (true) {

	if (initialized) {
	    // if you've read a frame into the packet, verify that you can extract info from it
	    if (process_frame(&packet_cp)) {
		return true;
	    // otherwise start over
	    } else {
		av_free_packet(&packet);
		initialized = false;
	    }
	}
	// TODO CONTINUE WORKING ON THIS PART
    }




}





int main(int argc, const char* argv[]) {
    // get arg path
    char *VIDEO_PATH = argv[1];
    initialize_ffmpeg(VIDEO_PATH);

    int64_t num_vectors = -1;
    int64_t prev_num_vectors = -1;
    char frame_type;
    vector<AVMotionVector> vectors;

    for (int frame_i = 1; read_frame(num_vectors, frame_type, vectors); frame_i++) {

    }

}










