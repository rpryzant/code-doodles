from collections import OrderedDict
from collections import defaultdict


def key(elements, key, applyfn):
    d = defaultdict(list)
    for i, k in enumerate(key):
        d[k].append(elements[i])
    return (map(applyfn, d.values()), d.keys())


def key_sum(e, k):
    return key(map(int, e.split()), map(int, k.split()), sum)


def key_hist(e):
    return key(map(int, e.split()), map(int, e.split()), len)


e = '3 4 5 6'
k = '2 0 1 2'
print key_sum(e, k)        
        

e = "5 3 5 2 2 9 7 0 7 5 9 2 9 1 9 9 6 6 8 5 1 1 4 8 5 0 3 5 8 2 3 8 3 4 6 4 9 3 4 3 4 5 9 9 9 7 7 1 9 3 4 6 6 8 8 0 4 0 6 3 2 6 3 2 3 5 7 4 2 6 7 3 9 5 7 8 9 5 6 5 6 8 3 1 8 4 6 5 6 4 8 9 5 7 8 4 4 9 2 6 10"
print key_hist(e)



