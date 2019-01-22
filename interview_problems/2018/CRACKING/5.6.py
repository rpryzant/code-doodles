
def count_different(a, b):
    a = a ^ b
    s = 0
    while a > 0:
        s += a & 1
        a >>= 1
    return s


print count_different(29, 15)
