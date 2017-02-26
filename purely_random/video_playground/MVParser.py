"""
=== TODO
- pair up images too for each frame


=== USAGE
python MVParser.py extractor frame_extract_test.mp4

"""
import subprocess
import numpy as np
import os
import sys
import re
import cv2

class MVParser(object):
    """ class that provides interface for parsing & accessing motion vectors from a video
    """

    def __init__(self, extractor_path, video_path):
        self.cur_dir = os.path.dirname(os.path.realpath(__file__))
        self.w, self.h = self.get_video_dimensions(video_path)
        self.extractor = extractor_path
        self.video = video_path

        self.frame_summaries = self.extract_mvs(extractor_path, video_path)


    def iter_frames(self):
        for i in range(1, self.num_frames() + 1):
            yield self.frame_vector_mapping[i]


    def num_frames(self):
        return len(self.frame_vector_mapping)


    def frame_info(self, i):
        return self.frame_vector_mapping[i]


    def get_video_dimensions(self, video):
        vcap = cv2.VideoCapture(video)
        width = vcap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)   # float
        height = vcap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT) # float
        return width, height    


    def extract_mvs(self, extractor, video):
        extractor_output = os.popen('./%s %s' % (extractor, video)).read()
        frames = extractor_output.split('#')
        out = {}
        for frame in frames:
            if not frame: continue
            ts, frame_i, frame_type, vector_count, vectors = self.parse_frame(frame)
            out[int(frame_i)] = {'type': frame_type,
                            'ts': ts,
                            'num': vector_count,
                            'vectors': vectors}
        return out


    def parse_frame(self, f):
        def parse_body(b):
            out = np.zeros([self.w, self.h, 2])
            for mv in b:
                if not mv: continue
                [x, y, dx, dy] = mv.strip().split(',')
                try:
                    out[int(x), int(y)] = [int(dx), int(dy)]
                except IndexError:
                    continue
            return out

        f = f.split('\n')

        header = f[0]
        header_regex = 'ts=(\d+),frame_i=(\d+),frame_type=([A-Z]),shape=(\d+)'
        ts, frame_i, frame_type, n = re.match(header_regex, header).groups()

        body_vectors = parse_body(f[1:] if len(f) > 1 else [])
        return ts, frame_i, frame_type, n, body_vectors


if __name__ == "__main__":
    mvp = MVParser(sys.argv[1], sys.argv[2])

