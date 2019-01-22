

def __combo(a, t, j, c, r):
    if t == 0:
        t = c[:]
        r.append(t)
        return
    for i in range(j, len(a)):
        if t < a[i]:
            return
        c.append(a[i])
        __combo(a, t - a[i], i, c, r)
        c.pop()


def combo(a, t):
    result = []
    if not a or t < 0:
        return result
    a = sorted(a)
    __combo(a, t, 0, [], result)
    return result

print combo([2,3,6,7], 7)
