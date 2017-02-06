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





AVFormatContext* pformat_context;
AVStream* pvideo_stream;
size_t frame_width;
size_t frame_height;
AVFrame* pframe;
int video_stream_index;


void initialize_ffmpeg(char *video_path) {
    // Initializes libavformat and registers all the muxers, demuxers and protocols
    av_register_all();

    // set up empty container frame/context to parse into
    pframe = av_frame_alloc();                      // https://www.ffmpeg.org/doxygen/2.7/structAVFrame.html
    pformat_context = avformat_alloc_context();     // https://ffmpeg.org/doxygen/2.7/structAVFormatContext.html
    video_stream_index = -1;

    // try to open input file
    if ((e = avformat_open_input(&pformat_context, video_path, NULL, NULL)) != 0)
	throw std::runtime_error("Couldn't open file!");

    // verify that input is video stream
    if ((e = avformat_find_stream_info(pformat_context, NULL)) < 0)
	throw std::runtime_error("Couldn't find stream info!");

    for (int i = 0; i < pformat_context->nb_streams; i++) {
	AVCodecContext *codec = pformat_context->streams[i]->codec;

	// skip to very start of video stream to grab metadata
	if (codec->codec_type == AVMEDIA_TYPE_VIDEO && video_stream_index < 0) {
	    AVCodec *p_codec = avcodec_find_decoder(codec->codec_id);
	    AVDictionary *operations = NULL;
	    av_dict_set(&operations, "flags2", "+export_mvs", 0);

	    if (avcodec_open2(codec, p_codec, &operations) < 0 || !p_codec)
		throw std::runtime_error("Couldn't open video codec!");

	    video_stream_index = i;                          // remember index where video stream starts
	    pvideo_stream = pformat_context->streams[i];     // remember this stream as primary video stream
	    frame_width = codec->width;                      // get frame width & height
	    frame_height = codec->height;

	    break;
	}
    }

    if (video_stream_index == -1)
	throw std::runtime_error("ffmpeg failed to initialize -- video stream info not found!");


}







int main(int argc, const char* argv[]) {
    // get arg path
    char *VIDEO_PATH = argv[1];

    initialize_ffmpeg(VIDEO_PATH);



}










