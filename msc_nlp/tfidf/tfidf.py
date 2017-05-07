"""
method for fast tfidf

"""
import purestemmer as Stemmer
import numpy as np
import math
from collections import Counter, defaultdict
import os


from scipy import spatial

class TFIDF:
    """ fast tf-idf calculation
        exposed methods are factory methods (overridden by subclasses)
    """
    def __init__(self, corpus=None, name='tfidf'):
        """ corpus = [documents]
            document = [words]
        """
        self.name = name
        self.stemmer = Stemmer.Stemmer('english')

        self.vocab = self.clean_doc(list(set([w for s in corpus for w in s])))  

        cleaned_corpus = [self.clean_doc(d) for d in corpus]

        self.idfs = self.build_idfs(cleaned_corpus)
        self.corpus_matrix = self.build_corpus_matrix(cleaned_corpus)


    def rank_corpus(self, query, max_results=20):
        """ query = [words]
            returns sorted [(cosine sim, index of match in corpus)]
        """
        query_tfidf = self.tfidf_vec(self.clean_doc(query))
        magnitude = np.sqrt(np.sum(query_tfidf ** 2))
        query_tfidf /= magnitude

        cos_sims = np.dot(query_tfidf, self.corpus_matrix)
        indices = np.arange(len(cos_sims))
        return sorted(zip(cos_sims, indices), reverse=True)[:max_results]


    def build_corpus_matrix(self, corpus):
        """ builds a bunch of tfidf vectors for the corpus
            where rows = vocab, cols = documents
        """
        vecs = [self.tfidf_vec(s) for s in corpus]
        matrix = np.array(vecs).T
        magnitudes = np.sqrt(np.sum(matrix ** 2, axis=0))
        return matrix / magnitudes   # length normalize


    def tfidf_vec(self, cleaned_doc):
        """ cleaned_doct = [words (cleaned)]
        """
        word_freqs = Counter(cleaned_doc)
        out = []
        for tok in self.vocab:
            idf = self.idfs[tok]
            tf = 1 + math.log(word_freqs.get(tok, 0.0001))    # TF
            out.append(tf * idf)
        return np.array(out)


    def build_idfs(self, corpus):
        """ the "idf" part of tf-idf
            technically "inverse document frequency smooth" because adding 1 to denom
        """
        idf_vals = {}
        for tok in self.vocab:
            docs_with_tok = sum(map(lambda s: tok in s, corpus))
            idf_vals[tok] = math.log(len(corpus) * 1.0 / (1.0 + docs_with_tok))
        return idf_vals


    def clean_doc(self, doc):
        return map(lambda x: self.clean_word(x), doc)


    def clean_word(self, word):
        return self.stemmer.stemWord(word.lower())


    @staticmethod
    def build_raw_tfidf(corpus, vocab=None):
        """ corpus = [documents]
            document = [words]

            spits out a new TFIDF instance
        """
        tfidf = TFIDF(corpus, vocab)
        return tfidf


    @staticmethod
    def build_file_tfidf(corpus, vocab=None):
        """ corpus = [file names]

            spits out a new TFIDF instance
        """
        corpus = map(lambda x: open(x).read().split(), corpus)
        tfidf = TFIDF(corpus, vocab)
        return tfidf




if __name__ == '__main__':
    # corpus = [
    #     ['Hello', 'my', 'name'],
    #     ['I', 'think', 'my'],
    #     ['Name', 'is', 'reid'],
    #     ['Running', 'is', 'my', 'Freeky']
    # ]
    # query = ['hello', 'my', 'name', 'is', 'reid']


    import sys
    corpus = ['test2.txt', 'test3.txt']
    tfidf = TFIDF.build_file_tfidf(corpus)

    query = open('test1.txt').read().split()

    print tfidf.rank_corpus(query) # should be 2, followed by 0



