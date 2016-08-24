


def get_even_mask():
    out = 0
    for i in range(32)[::2]:
        out += 2 ** i
    return out

def swap_bits(n):
    mask = get_even_mask()
    out = 0
    # bring even bits over
    out |= (mask & n) << 1
    # bring odd bits over
    out |= ((mask << 1) & n) >> 1
    return out


print swap_bits(25)
