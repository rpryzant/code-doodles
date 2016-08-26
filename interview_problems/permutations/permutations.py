

def insert_everywhere(x, l):
    out = []
    for i in range(len(l)+1):
        t = l[:]
        t.insert(i, x)
        out.append(t)
    return out

def permutations(a):
    if len(a) <= 1:
        return [a]
    tmp = permutations(a[1:])
    p = []
    for permutation in tmp:
        p += insert_everywhere(a[0], permutation)
    return p

print permutations([1,2,3])
