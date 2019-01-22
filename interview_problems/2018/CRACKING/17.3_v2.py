import random
from collections import defaultdict


def choose(a, k):
    assert k <= a

    chosen = set([])

    def select():
        i = int(random.random() * len(a))
        while i in chosen:
            i = int(random.random() * len(a))
        chosen.add(i)
        return i

    return [select() for _ in range(k)]


counts = defaultdict(int)
for _ in range(100000):
    for chosen in choose(range(10), 3):
        counts[chosen] += 1
print counts
