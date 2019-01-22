# this is cleaner!!!


from collections import defaultdict
from random import randrange



RAND_MAX = 100


def rand():
    return randrange(0, RAND_MAX)


def rand_range(l, r):
    rng = r - l + 1
    while True:
        n = rand()
        if n < (RAND_MAX / rng) * rng:
            return (n % rng) + l

d = defaultdict(lambda: 0)
for _ in range(10000):
    d[rand_range(5, 19)] += 1


print d
