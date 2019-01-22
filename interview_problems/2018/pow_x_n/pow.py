
# pre: n >= 0
def powR(x, n):
    if n == 0:
        return 1
    v = powR(x, n/2)
    if n % 2 == 0:
        return 2 * v
    return x * v * v

def pow(x, n):
    if n < 0:
        return 1.0 / powR(x, -n)
    else:
        return powR(x, n)


print pow(2, 7)
print pow(2, -2)
print pow(2, 31)
