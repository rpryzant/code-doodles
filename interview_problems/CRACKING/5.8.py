

def draw(a, w, x1, x2, y):
    if w % 8:
        return None
    m = w/8
    if len(a) % m:
        return None
    n = len(a) / m
    if x1 >= w or x2 >= w or y >= n:
        return None
    for i in range(x1, x2):
        set_bit(a, (y*m)+(i/8), 8 - (i%8) - 1)
    return a


def set_bit(a, index, bit):
    a[index] |= 1 << bit


test = [0,0,0,0,0,0,0,0,0]

a = draw(test, 24, 10, 20, 1)

print [bin(l) for l in a]    
print a



