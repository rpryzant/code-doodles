from collections import Counter


def is_permutation(a, b):
    if len(a) != len(b):
        return False
    ca = Counter(a)
    cb = Counter(b)

    return set(ca.items()) == set(cb.items())

print is_permutation("great", "rgtae")
print is_permutation("great", "rgtge")
