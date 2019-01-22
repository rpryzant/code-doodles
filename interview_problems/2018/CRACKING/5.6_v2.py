"""
xor: 
1 1   -
1 0   1
0 1   1
0 0   -


"""

def count_diff(a, b):
    s = 0
    while a > 0 or b > 0:
        s += (a & 1) ^ (b & 1)
        a >>= 1
        b >>= 1
    return s

#          1111 
#         11101 
print count_diff(29, 15)
