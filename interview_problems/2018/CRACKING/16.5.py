

def count_trailing(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    c = 0
    while f % 10 == 0:
        c += 1
        f /= 10
    return c





print count_trailing(5)
