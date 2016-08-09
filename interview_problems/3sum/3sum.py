



def gen_3sums(a):
    a = sorted(a)
    for i, x in enumerate(a):
        for j, y in enumerate(a):
            k = bsearch(a, -(x+y))
            if k:
                yield i, j, k


def bsearch(a, t):
    l = 0
    h = len(a) - 1
    while l <= h:
        m = (l + h) / 2
        if t > a[m]:
            l = m+1
        elif t < a[m]:
            h = m-1
        else:
            return m
    return None
