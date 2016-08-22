


def __cs(a, t, j, c, r):
    if t == 0:
        tmp = c[:]
        r.append(tmp)
        return
    for i in range(j+1, len(a)):
        if a[i] > t:
            return
        c.append(a[i])
        __cs(a, t-a[i], i, c, r)
        c.pop()

def cs(a, t):
    result = []
    if not a or t < 0:
        return result
    a = sorted(a)
    cur = []
    __cs(a, t, -1, cur, result)
    return result


print cs([10, 1, 2, 7, 6, 1, 5], 8)
