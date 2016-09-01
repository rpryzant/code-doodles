from random import random
from collections import defaultdict

# soln A: bucket random variable X \in [0, 1] dynamically
# X is guarenteed to be <= 100 and P is guarenteed to sum to 1
# faster than soln B if |P| < 100 (probable) and if you're only going 
# to be drawing from the distribution a few times
def bucket(P, X):
    X *= 100
    sum = 0
    for level, p in enumerate(P):
        sum += p
        if X <= sum:
            return level
    return -1


# soln B: build lookup table from integers to buckets
# then bucket X according to d[int(X * 100)]
# takes longer at the onset but better if this method is going to be called repeatedly
#  cause it's essentially caching f: R => N
def build_lookup(P):
    d = {}
    ptr = 0
    sum = P[0]
    for i in range(101):
        if i > sum:
            ptr += 1
            sum += P[ptr]
        d[i] = ptr
    return d


def draw(P, C):
    return C[bucket(P, random())]


P  =[ 15, 25, 40, 20 ]
X = [ 'a', 'x', 'z', 'b' ]
d = defaultdict(lambda: 0)
for _ in range(10000):
    d[draw( P, X)] += 1

print '\n'.join('%s %s' % (k, v) for (k, v) in zip(P, X))
s = sum(d.values())
for k in d:
    print float(d[k]) / s, k
