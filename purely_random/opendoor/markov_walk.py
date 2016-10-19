# send to mike@opendoor

from collections import defaultdict
import random
from bisect import bisect_right





def search_dist(a, d):
    i = bisect_right(a, d)
    return i



# O(E + NV) 
def walk(trans_probs, n, start_state):
    R = defaultdict(list)


    # O(E)
    for prob in trans_probs:
        R[prob[0]].append((prob[1], prob[2] if R[prob[0]] == [] else prob[2] + R[prob[0]][-1][1]))

    def step(s):
        r_dist = R[s]
        draw = random.random()
        s = 0
        return r_dist[search_dist([x[1] for x  in r_dist], draw)][0]


    counts = defaultdict(int)
    cur_state = start_state
    counts[cur_state] += 1
    #O(N)
    for _ in range(n):
        cur_state = step(cur_state)
        counts[cur_state] += 1

    return counts
                       


trans_probs = [
    ('a', 'a', 0.9),
    ('a','b',0.05),
    ('a','c',0.05),
    ('b','b',0.5),
    ('b','a',0.25),
    ('b','c',0.25),
    ('c','c',0.9),
    ('c','a',0.1)
]



print walk(trans_probs, 1000, 'a')
