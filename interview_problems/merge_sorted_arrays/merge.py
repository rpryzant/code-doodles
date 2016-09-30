

def merge(a, m, b, n):
    if m < 0 or n < 0 or a is None or b is None:
        return a
    ai = bi = 0
    while bi < len(b):
        if b[bi] <= a[ai]:
            a.insert(ai, b[bi])
            m += 1
            bi += 1
        elif ai >= m:
            a[ai] = b[bi]
            bi += 1
        ai += 1
    return a

print merge([1,2,3,8,0,0,0,0], 4, [2, 9], 2)
