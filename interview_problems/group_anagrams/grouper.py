# nice! this is O(nk) 
# soln online was O(n * k log k) + O(n log n)
from collections import defaultdict


def count_chars(s):
    h = defaultdict(lambda: 0)
    for c in s:
        h[c] += 1
    return h

def group(a):
    matches = defaultdict(list)
    for s in a:
        hist = count_chars(s)
        matches[(tuple(hist.keys()), tuple(hist.values()))].append(s)
    return [sorted(x) for x in matches.values()]


print group(["eat", "tea", "tan", "ate", "nat", "bat"])
