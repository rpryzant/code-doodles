
# extract all I frames to seperate files
ffmpeg -i $1 -vf "select='eq(pict_type,PICT_TYPE_I)'" -vsync vfr thumb%04d.png



