CFLAGS = -O3 -D__STDC_CONSTANT_MACROS
LDFLAGS = -lswscale -lavdevice -lavformat -lavcodec -lswresample -lavutil -lpthread -lbz2 -lz -lc -lrt
INSTALLED_DEPS = -Idependencies/include -Ldependencies/lib

extractor: extractor.cpp
	g++ $< -o $@ $(CFLAGS) $(LDFLAGS) $(INSTALLED_DEPS)
