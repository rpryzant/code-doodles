
"""
input : query log
query1
...
queryn    (n ~1M)


return top 10 queries (by frequency)
no ordering on queries


=============== THINKING/NOTES  ========================


shrink problem

n = 100?

1) sort queries, count matching adjacents

2) count frequencies of ALL words, return top k
      throwing in dict
      put the keys into a max heap of size k
      give max ehap

roger.luo@snapchat.com

"""
import sys
import collections
import heapq


K = int(sys.argv[2])
f = open(sys.argv[1])


freqs = collections.Counter(line.strip() for line in f)
min_heap = []

for query, freq in freqs.items():
    if len(min_heap) < K:
        heapq.heappush(min_heap, (freq, query))
    elif freq < min_heap[-1]:
        heapq.heappushpop(min_heap,(freq, query))

# my results
print [x for x in min_heap]
# verification
print sorted(freqs.items(), key=lambda x: x[1], reverse=True)[:K]



    

