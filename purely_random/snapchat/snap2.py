log

s1
s2
…
sn

return k most frequently occuring strings in this log 


IDEAS

shrink problem
sort list, find adjacents 
O(n log n)
get word freqs, then use heap
word freqs is O(n) time (& space)
use heap to track top k

heaps?
max? min?
if max, then biggest is at top of list
heaps have depth of log_2(len(h)
                          and the last 2^depth nodes might be min

if min, then smallest is at top of list
                          if len(h) > k, we can boot that smallest element
                          and are guarenteed that h always holds top k elems
















from collections import Counter
import heapq
                          
def parse_logs(f, k):

c = Counter([s.strip() for s in open(f).readlines()])
                          
                          heap = []
                          for line, count in c.iteritems():
                              heapq.heappush(heap, (count, line))
                          if len(heap) > k:
                              heapq.heappop(heap)

return map(lambda c, l: l, sorted(heap))





