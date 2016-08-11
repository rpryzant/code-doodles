from heapq import heappush, heappop


def merge_k(l):
    return [x for x in gen_min(l)]

def gen_min(l):
    heap = []
    for i, list in enumerate(l):
        heappush(heap, (list[0], (i, 0)))
    while heap:
        x, (i, k) = heappop(heap)
        yield x
        if k < len(l[i])-1:
            heappush(heap, (l[i][k+1], (i, k+1)))


l = [
    [2,6,22],
    [1,20],
    [19,23,50],
    [4,9,10]
]

print merge_k(l)
