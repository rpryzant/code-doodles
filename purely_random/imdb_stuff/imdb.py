import urllib2
import json

def search(query):
    get_url = 'http://theapache64.xyz:8080/movie_db/search?keyword=%s' % query
    response = urllib2.urlopen(get_url).read().decode('utf-8')
    return json.loads(response)




