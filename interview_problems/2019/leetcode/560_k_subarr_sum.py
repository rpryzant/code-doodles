"""
get num of subarrays whose sum == tgt


are elements negative?  yes
integers? yes
bounds on subarr size?


consecutive subarrays? yes




1) brute

all subarrays, check sum  (n^2)


2) multi pass?

from front: can get
ai = sum(x[:i])

[ t-sum(a[0])  t-sum(a[:1]), ..., t-sum(a[:i]), ..., t-sum(a) ]


"""
from collections import defaultdict 

def k_subarr(a, t):
    remainder_counts = defaultdict(int)
    partial_sum = 0
    for x in a:
        partial_sum += x
        remainder_counts[partial_sum] += 1

    out = 0
    partial_sum = 0
    for x in a:
        partial_sum += x
        out += remainder_counts[t - partial_sum]

    return out
