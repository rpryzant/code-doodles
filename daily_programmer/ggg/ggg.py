import sys
from collections import defaultdict
import Queue

# [1, 2, 3, 4, ...] => [(1, 2), (3, 4), ...]
def pairs(l):
    l = iter(l)
    return zip(l, l)

def decode(encoding, msg, key = None):
    if not key:
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

def encoding_for_tree(node, coding, key):
    if isinstance(node[1], str):
        key[node[1]] = coding
    else:
        encoding_for_tree(node[1], coding + 'g', key)
        encoding_for_tree(node[2], coding + 'G', key)

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
    key = {}
    encoding_for_tree(pq.get(), '', key)
    print key
    return ''.join(key.get(c, c) for c in msg)
    # TODO - FINISH IMPLEMENTING HUFFMAN
    



with open(sys.argv[1]) as file:
#    print decode(file.readline().strip(), file.readline().strip())
    print encode("hello, world!")
