import sys
import re


limit = int(sys.argv[2])

def gen_words(f):
    for line in open(sys.argv[1]):
        if line == '\n':
            yield line
        else:
            for word in line.strip().split():
                yield word

c = 0
s = ''
for word in gen_words(sys.argv[1]):
    if c + len(word) <= limit:
        s += '%s' % word
        c += len(word)
    else:
        print s
        c = len(word)
        s = word
    if c < limit:
        s += ' '
        c += 1
print s
