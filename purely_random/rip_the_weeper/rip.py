"""
gave up on this once i realized bandbamp redirects its "download links"

"""

import sys
import os
import re

def download_mp3s(url):
    """ pulls down all the mp3s linked to on a bandcamp page
    """
    def gen_urls(bandcamp_html):
        f = open(bandcamp_html)
        tracks = re.findall('(\[.*?\])', f.read())[0]
        tracks.replace('null', 'None').replace('false', 'False')
        tracks = eval(tracks)       # WARNING!! VERY INSECURE

        for track in f:
            yield track['title'], track['file']['mp3-128']


    # dl page
    os.system('wget %s -O ~/tmp')
    os.system('grep "trackinfo:" ~/tmp > ~/tmp2')
    for title, url in gen_urls('~/tmp2'):
        






url = sys.argv[1]



download_mp3s(url)
