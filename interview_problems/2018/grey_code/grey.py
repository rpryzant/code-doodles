# in notes


def grey_code_seq(n):
    out = []
    for i in range(n+1):

        out.append(b2s(n2g(i)))
    return out


def b2s(n):
    s = ""
    while n > 0:
        s = ('1' if n & 1 == 1 else '0') + s
        n >>=1
    return s

def n2g(n):
    print n, b2s(n), b2s(msb(n))
    return (n ^ (n >> 1))


def msb(n):
    mask = 1 << 31
    while n & mask == 0 and mask > 0:
        mask >>= 1
    return mask



print grey_code_seq(7)
