


# assuming python 2.7...
def divide_and_round(a, b, N):
    frac = a * 1.0 / b
    return str(round(frac, N))

def divide_and_round2(a, b, N):
    frac = a * 1.0 / b
    out = '%s.' % int(frac % 10)
    for i in range(1, N + 1):
        frac *= 10
        out += str(int(frac % 10))
    return out



print divide_and_round2(5, 3, 5)
print divide_and_round2(5, 3, 2)
