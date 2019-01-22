



def two_sum(l, t):
    d = {t - x: (i, x) for i, x in enumerate(l)}
    (i1, x1), (i2, x2) = next((((i, x), d.get(x)) for i, x in enumerate(l) if d.get(x) is not None))
    return min(i1, i2) + 1, max(i1, i2) + 1


l = [2, 7, 11, 15]
t = 9

print two_sum(l, t)

    
