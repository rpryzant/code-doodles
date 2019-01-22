"""           
[4 5 7 8 ]
   ^

[1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
     ^             ^
     --------

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

 4

1
sort and return 
O(n log n)

2
O(n)
min heaps
if running window, can always lay down smallest of window
what’s that window?
if k:
time: O(n log (k+1))
space: O(n)

import heapq
[1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
                           1   2   3

n + (k + 1)












[1, 4, 5, 2, 3, 7, 8]           k = 2
                            ^ 
                                len = 10,  12                
i  12   
out    1  2  3 4 5 7  8
heap  

"""
def sortKMessedArray(a, k):
out = []
heap = []
// i=k,  i=len+k-1
// len
for i in range(len(a) + k):
    if i < k:
        heapq.heappush(heap, a[i])
    elif i >= len(a):
        out.append(heapq.heappop(heap)
                   else:
out.append(heapq.pushpop(heap, a[i])
           return out




heap = a[:k]
heapq.heapify(heap)

           for i in range(k, len(a)):
               # len(heap) == k
           lowest = heapq.pushpop(heap, a[i])
           out.append(lowest)

           while len(heap) > 0:
               out.append(heapq.heappop(heap))

           return out
# best!!
def sort(a, k):
    for i in xrange(0, k)
           heap.push(a[i]);
    for i in xrange(0, n)     
           if (i+k < len) heap.push(a[i+k]);     
           out.append(heap.pop())


