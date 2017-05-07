import sys
from nltk.tokenize import sent_tokenize
from collections import Counter
import purestemmer as Stemmer
import string



class Summarizer:

    def __init__(self, stopfile, k=5, n=5):
        self.stemmer = Stemmer.Stemmer('english')

        self.stops = self.parse_stopfile(stopfile)

        self.k = k
        self.n = n

    def clean_w(self, w):
        w = w.strip()
        w = w.translate(None, string.punctuation).lower()
        return self.stemmer.stemWord(w)

    def clean_s(self, s):
        return [self.clean_w(w) for w in s.split() \
                    if self.clean_w(w) not in self.stops]

    def parse_stopfile(self, stopf):
        return set([self.clean_w(w) \
                        for s in open(stopf).readlines()\
                        for w in s.split()])
    
    def flatten(self, l):
        return [w for s in l for w in s]

    def score(self, s, pivots):
        return sum([pivots.get(w, 0) for w in s])

    def summarize(self, f):
        raw_doc = sent_tokenize(open(f).read())
        doc = map(lambda s: self.clean_s(s), raw_doc)
        pivots = Counter(self.flatten(doc)).most_common(self.k)
        scores = map(lambda s: self.score(s, dict(pivots)), doc)
        top_sentences = sorted(zip(scores, range(len(scores))), reverse=True)[:self.n]
        return [raw_doc[i] for score, i in top_sentences]


if __name__ == '__main__':
    input = 'example.txt'
    stops = 'stop_words.txt'

    summarizer = Summarizer(stops)
    print summarizer.summarize(input)
