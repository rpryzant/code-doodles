

import math



# make alternating mask1  1010101010   int(log_2 X)
# make opposing mask2     0101010100
# fill mask1 with X        mask1 = mask1 & X
# fill mask2 with X        mask2 = mask2 & X

# result = (mask1 >> 1) + (mask2 << 1)

def flip_bits(x):
    odd_mask = sum(2 ** i for i in range(int(math.log(x, 2))+1)[::2])
    out = 0
    out |= (odd_mask & x) << 1
    out |= ((odd_mask << 1) & x) >> 1
    return out


print flip_bits(25)
