import sys
from collections import defaultdict
import Queue

# [1, 2, 3, 4, ...] => [(1, 2), (3, 4), ...]
def pairs(l):
    l = iter(l)
    return zip(l, l)

# parses an encoding (if given) or uses a pre-parsed key to decode a message
def decode(msg, key):
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

# parses encoding string into a dict
def key_from_encoding(encoding):
    return {k:v for v, k in pairs(encoding.split())}

# conducts dfs on a freq tree, creating a binary encoding as it goes
def encoding_for_tree(node, coding, key):
    if isinstance(node[1], str):
        key[node[1]] = coding
    else:
        encoding_for_tree(node[1], coding + 'g', key)
        encoding_for_tree(node[2], coding + 'G', key)

# generates a huffman encoding scheme for a message
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
    return ''.join(key.get(c, c) for c in msg)

encoding, message = tuple(open(sys.argv[1]).read().strip().split('\n'))
print "Input message: \n\t%s" % message
print "Decoding the sample file...with given encoding"
decoding = decode(message, key_from_encoding(encoding))
print "Decoded message:\n\t%s" % decoding
print "Huffman encoding of this message:\n\t%s" % encode(decoding)

