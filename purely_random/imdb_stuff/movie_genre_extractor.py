"""
runs through a file of title names and extracts
  imdb genre info
"""
import urllib
from bs4 import BeautifulSoup
import sys
import collections
from tqdm import tqdm


def gen_imdb_genres(query):
    # query imdb 
    url = 'http://www.imdb.com/find?s=all&q=%s' % urllib.quote(query)
    r = urllib.urlopen(url).read()
    s = BeautifulSoup(r)

    # select top hit
    table = s.findAll('table', {'class': 'findList'})[0]
    top_hit = table.find_all('tr')[0]
    url = top_hit.findAll('a')[-1]['href']

    # get genre info
    url = 'http://www.imdb.com/' + url
    r = urllib.urlopen(url).read()
    s = BeautifulSoup(r)
    g = s.findAll('div', {'class': 'see-more inline canwrap'})[-1]
    genres = g.findAll('a')

    for x in genres:
        yield x.text.strip().lower()


counts = collections.defaultdict(lambda: 0)
lines = map(lambda x: x.strip(), open(sys.argv[1]).readlines())

for l in tqdm(lines, total=len(lines)):
    try:
        for g in gen_imdb_genres(l.strip()):
            counts[g] += 1
    except:
        continue

print counts

