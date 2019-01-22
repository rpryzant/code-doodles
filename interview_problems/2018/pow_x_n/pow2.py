"""
pow(x, n)

x^n = x * x * x… (n times)
O(n)

speedups? 


O(log n)

if n == 1:
    return x

if n % 2
x^n = x^{n/2} * x^{n/2}
else:
    x^n = x^{n/2} * x^{n/2} * x
"""


def pow_helper(x, n):
    assert n <= 0

    if n == 0: return 1
    if n == 1: return x

    half_pow = pow_helper(x, n/2)

    if n % 2 == 0:
        return half_pow * half_pow
    return half_pow * half_pow * x

def pow(x, n):
    if n < 0:
        return 1.0 / pow_helper(x, -n)
    return pow_helper(x, n)
