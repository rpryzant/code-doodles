from collections import defaultdict

def is_permutation(s1, s2):
    d1 = hist(s1)
    d2 = hist(s2)
    return len(set(d1.items()) ^ set(d2.items())) == 0

def hist(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    return d


print is_permutation("great", "rgtae")
print is_permutation("great", "rgtge")
