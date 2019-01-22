


def sl(a, t, l, h):
    if l > h:
        return -1
    m = (l + h) / 2
    if a[m] == t and (m == 0 or a[m - 1] != t):
        return m
    if t > a[m]:
        return sl(a, t, m + 1, h)
    else:
        return sl(a, t, l, m - 1)

def sr(a, t, l, h):
    if l > h:
        return -1
    m = (l + h) / 2
    if a[m] == t and (m == len(a) - 1 or a[m + 1] != t):
        return m
    if t < a[m]:
        return sr(a, t, l, m - 1)
    else:
        return sr(a, t, m + 1, h)

def s(a, t):
    return sl(a, t, 0, len(a) - 1), sr(a, t, 0, len(a) - 1)

test = [5, 7, 7, 8, 8, 10]
print s(test, 8)
