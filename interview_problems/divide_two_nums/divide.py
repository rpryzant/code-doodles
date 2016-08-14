def divide(n, d):
    if d == 0:
        return None
    r = 0
    while (n - d) >= 0:
        n -= d
        r += 1
    return r



print divide(230, 7)
print divide(230, 0)
