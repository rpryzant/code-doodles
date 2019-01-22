from collections import defaultdict

# if defaultdicts
def merge(da, db):
    for k in db:
        da[k] += db[k]

# if not defaultdicts
def merge(da, db):
    for k in db:
        if da.get(k, False):
            da += db[k]
    for k in set(db.keys()) - set(da.keys()):
        da[k] = db[k]


d = defaultdict(lambda: 0)

def get_word_freq(book, word):
    if len(d) == 0:
        for word in book:
            d[word] += 1
    return d[word]
