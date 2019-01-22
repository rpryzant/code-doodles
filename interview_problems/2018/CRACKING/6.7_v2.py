import random
from collections import defaultdict

N = 10000
BOY = 'b'
GIRL = 'g'

def is_girl():
    return random.random() < 0.5

def make_family():
    out = [is_girl()]
    while not out[-1]:
        out.append(is_girl())
    print out
    return [GIRL if girl else BOY for girl in out]


counts = defaultdict(int)
for _ in range(N):
    for child in make_family():
        counts[child] += 1

print counts[BOY] * 1.0 / counts[GIRL]
