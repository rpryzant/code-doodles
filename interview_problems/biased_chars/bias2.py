"""
are we calling this once, or many? 
   are the p's changing or c's? or both? 

0 probs?

boom lol

"""
import random
import bisect



def draw(p, c):
    assert sum(p) == 100 and all([x >= 0 for x in p])
    partial_sums = [sum(p[:i+1]) for i in range(len(p))]
    return c[bisect.bisect_left(partial_sums, random.random() * 100)]


p = [15, 25, 40, 20]
c = [1,2,3,4,5]


from collections import defaultdict
counts = defaultdict(int)

for _ in range(100000):
    counts[draw(p, c)] += 1

print counts

