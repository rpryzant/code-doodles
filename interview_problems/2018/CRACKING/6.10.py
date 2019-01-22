# this one is good!!

from random import random

class Bottle:
    def __init__(self):
        self.poisened = False

    def poisen(self):
        self.poisened = True

    def is_poisened(self):
        return self.poisened

class Strip:
    def __init__(self):
        self.pos = False

    def test(self, bottles):
        for bottle in bottles:
            if bottle.is_poisened():
                self.pos = True

    def is_pos(self):
        return self.pos


def init_bottles(n):
    b =  {i: Bottle() for i in range(n)}
    index = int(random() * n)
    b[index].poisen()
    print index
    return b

def init_strips(m):
    return [Strip() for _ in range(m)]

DAYS_IN_WEEK = 7

def test(b, s, r):
    # bps = bottles_per_strip
    bps = (r[1] - r[0]) / len(s)
    for i, strip in enumerate(s):
        test_range = (r[0] + (i * bps), r[0] + (i * bps) + bps)
        strip.test([b[j] for j in range(*test_range)])
        if strip.is_pos():
            return test_range
    return None

def simulate(n, m, bottles = None, strips = None):
    if not bottles:
        bottles = init_bottles(n)
    if not strips:
        strips = init_strips(m)
    days = 0
    rng = (0, len(bottles))
    while rng[1] - rng[0] > 0:
        rng = test(bottles, strips, rng)
        days += DAYS_IN_WEEK
    return days, rng[0]






def gen_ones(n):
    i = 0
    while n > 0:
        if n & 1:
            yield i
        n >>= 1
        i += 1

def test_better(b, s):
    for k in b:
        for i in gen_ones(k):
            s[i].test([b[k]])


def strips_to_index(s):
    out = 0
    for i, strip in enumerate(s):
        if strip.is_pos():
            out += 2 ** i
    return out

def simulate_better(n, m, bottles = None, strips = None):
    if not bottles:
        bottles = init_bottles(n)
    if not strips:
        strips = init_strips(m)
    test_better(bottles, strips)
    return strips_to_index(strips)
                  

n = 1000
m = 10
b = init_bottles(n)
s = init_strips(m)
print simulate(n, m, b, s)
print simulate_better(n, m, b, s)
