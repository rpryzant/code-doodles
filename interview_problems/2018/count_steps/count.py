
# in notes

def count(n):
    return countDP(n, [-1 for _ in range(n+1)])


def countDP(n, m):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif m[n] > -1:
        return m[n]
    m[n] = countDP(n-1, m) + countDP(n-2, m)
    return m[n]


print count(15)
print count(3)
