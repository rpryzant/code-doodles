

def reverse(x):
    out = 0
    neg = False
    if x < 0:
        neg = True
        x = abs(x)
    while x > 0:
        out += x % 10
        x /= 10
        if x > 0:
            out *= 10
    if neg:
        return -out
    return out


print reverse(123)
print reverse(-123)
