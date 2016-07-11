import sys
from collections import defaultdict
import Queue

# [1, 2, 3, 4, ...] => [(1, 2), (3, 4), ...]
def pairs(l):
    l = iter(l)
    return zip(l, l)

def decode(msg):
    key = {k:v for v, k in pairs(encoding.split())}
    tmp = ''
    decoded = ''
    for char in msg:
        if char.lower() == 'g':
            tmp += char
            if key.get(tmp):
                decoded += key[tmp]
                tmp = ''
        else:
            decoded += char
    return decoded

def encode(msg):
    freqs = defaultdict(int)
    for char in msg:
        if char.isalpha():
            freqs[char] += 1
    pq = Queue.PriorityQueue()
    for char in freqs:
        pq.put((freqs[char], char))
    while pq.qsize() > 1:
        left, right = pq.get(), pq.get()
        pq.put((left[0] + right[0], left, right))
    print pq.get()
    # TODO - FINISH IMPLEMENTING HUFFMAN
    



with open(sys.argv[1]) as file:
#    print decode(file.readline().strip())
    print encode("hello, world!")
