# my solution is more valid than that in the book! I like my solution!




import random
import collections


def choose(l, m):
    selected = {}
    for _ in range(m):
        n = select(l, selected)
        selected[n] = True
    return selected.keys()


def select(l, selected):
    x = l[int(random.random() * len(l))]
    while x in selected:
        x = l[int(random.random() * len(l))]
    return x



d = collections.defaultdict(float)

for _ in range(10000):
    for chosen in choose([1,2,3,4,5,6,7,8,9,10], 3):
        d[chosen] += 1


print d
