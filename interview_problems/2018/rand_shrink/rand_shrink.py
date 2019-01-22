
from collections import defaultdict
from random import randrange


#RAND_MAX = (2 ** 31) - 1
RAND_MAX = 100


def rand():
    return randrange(0, RAND_MAX)


def rand_range(r, l):
    range = r - l + 1
    offset = (RAND_MAX % range) + 1
    
    n = rand()
    while n > RAND_MAX - offset:
        n = rand_int()
    return (n % range) + l


d = defaultdict(lambda: 0)
for _ in range(1000000):
    d[rand_range(5, 19)] += 1


print d
