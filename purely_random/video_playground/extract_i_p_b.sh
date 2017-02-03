


# http://www.di.ens.fr/willow/pdfscurrent/kantorov14cvpr.pdf
# https://github.com/vadimkantorov/mpegflow




# extract all I frames to seperate files
ffmpeg -i $1 -vf "select='eq(pict_type,PICT_TYPE_I)'" -vsync vfr i_thumb%04d.png;

# P frames
ffmpeg -i $1 -vf "select='eq(pict_type,PICT_TYPE_P)'" -vsync vfr p_thumb%04d;

# B frames
#ffmpeg -i $1 -vf "select='eq(pict_type,PICT_TYPE_B)'" -vsync vfr b_thumb%04d.png;



# viz motion vectors
# ffmpeg -debug vis_mb_type -i frame_extract_test.mp4 out.mp4