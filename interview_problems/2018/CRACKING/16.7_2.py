# this is beter!!!!!!! woot :)
"""

relaxing constraints

return max(a, b)

tightening somewhat: no max()

SIGN_BIT = 32


def is_neg(x):
    return (x & (1 << SIGN_BIT)) >> SIGN_BIT

apos = a > 0
bpos = b > 0

if not apos and not bpos:
    if -a + b > 0:
        return b
    else:
        return a
elif not apos:
    return b
elif not bpos:
    return a
else:
    if a - b > 0:
        return a
    else:
        return b

but no if-else!!!













proxies for if-else
dictionary lookup -- subtract, take whichever has 1 in sign? 
ALWAYS (max - min) is positive
ALWAYS (min - max) is negative
a - b
get sign bit (has to be 0 or 1)
d[0] = a
d[1] = b

5 3
3 5
if a & b positive and a > b: 
    (a-b)      (b-a)
       2          -2 *one in sign bit
5 -3

if a pos, b neg a > b
      (a-b)      (b-a)
                   -8 *one in sign
-5 3
a neg, b pos b > a
(a-b)      (b-a)
    *one in sign

-5 -3
a neg, b neg b > a
      (a - b)    (b - a)
        -2          2
    *one in sign
"""

def my_max(a, b):
    def get_sign(x):
        return (x & (1 << 32)) >> 32
    dif = a - b
    sign_dif = get_sign(dif)
    d = {0: a, 1: b}
    return d[sign_dif]

print my_max(5, 3)
print my_max(3, 5)
print my_max(3, -5)
print my_max(-3, -5)
print my_max(-3, 5)
