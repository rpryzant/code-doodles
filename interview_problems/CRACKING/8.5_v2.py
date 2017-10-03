

"""
recursive multiply

break into cases

x * y

if y == 0: return 0

if y == 1: return x

if y is a power of 2: return x << log(y, 2)

if y is divisible by 2:
   xy = x((y/2) (y/2)) = 2 * x(y/2)

when all else fails:
   xy = x * (x(y-1))

"""
import math

def mul(a, b):
    def recurse(x, y):
        if y == 0: return 0
        elif y == 1: return x
        elif y & (y - 1) == 0:
            return x << int(math.log(y, 2))
        elif y % 2 == 0:
            halfprod = recurse(x, y/2)
            return halfprod * halfprod
        else:
            return x * recurse(x, y - 1)
    return recurse(a, b) if a >= b else recurse(b, a)


print mul(8, 9)






