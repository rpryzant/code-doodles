import math


def perms(n, k):
    s = []
    a = range(1, n+1)
    for _ in range(n):
        idx = ((k-1) / math.factorial(len(a) - 1)) % len(a)
        s.append(a.pop(idx))

    return ''.join(str(i) for i in s)

print perms(3, 4)
print perms(3, 6)
print perms(3, 2)



