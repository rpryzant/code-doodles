# -*- coding: utf-8 -*-
"""
combo sum

choose numbers from c that add up to t

is c sorted?
no => sort first because only need to check up to t/2 
yes => great
no set dups allowed
dups in c? no (if yes, rm)


1
dfs
for i in len(sorted(c))
see if there’s a soln to c[i:] using t - c[i]
O(t) space


2 points of slowness (1?)
when we 

====================================================
"""

def combos(c, t):
    c = sorted(c)
    out = []

    def recurse(sofar, c_r, t_r):
        if len(c_r) == 0 or t_r < 0:
            return
        if t_r == 0:
            out.append(sofar[:])

        for i in range(len(c_r)):
            sofar.append(c_r[i])
            recurse(sofar, c_r[i:], t_r - c_r[i])
            sofar.pop()

    recurse([], c[:], t)
    return out

print combos([2,3,6,7], 7)


# FASTER!!!
def combos2(c, t):
    c = sorted(c)
    out = []

    def recurse(sofar, i, t_r):
        if t_r < 0:
            return
        if t_r == 0:
            out.append(sofar[:])
        for j in range(i, len(c)):
            if c[j] > t:
                return
            sofar.append(c[j])
            recurse(sofar, j, t_r - c[j])
            sofar.pop()

    recurse([], 0, t)
    return out

print combos2([2,3,6,7], 7)

