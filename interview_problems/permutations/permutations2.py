"""all permutations

(k-1)! perms
n1 n2 ..  nk

if we have 
[  all permutations of 1st k-1 numbers ]

then we duplicate that list k-1 times, and insert nk into a different 
index for each duplication

1 2 3
    ^

[[2, 1], [1, 2]], 3
"""


def insert_everywhere(l, x):
    out = []
    for i in range(len(l[0])+1):
        tmp = [a[:] for a in l]
        map(lambda a: a.insert(i, x), tmp)
        out += tmp
    return out


def permutations(arr):
    sofar = [[]]
    for x in arr:
        sofar = insert_everywhere(sofar, x)
    return sofar




print permutations([1,2,3])
