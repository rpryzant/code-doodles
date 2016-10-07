

def sum_swap(A, B):
    c = abs(sum(A) - sum(B))
    if c % 1:
        return None
    d = {c - a: a for a in A}
    for b in B:
        if d.get(b):
            return d[b], b
    return None



print sum_swap( [3,6,3,3], [4,1,2,1,1,2])
print sum_swap([4,1,2,1,1,2], [3,6,3,3])

