

SIGN_MASK  =  1 << 32

def max_old(a, b):
    if (a - b) & SIGN_MASK:
        return b
    return a



def max_with_overflow(a, b):
    # overflow would be caused by different signed params
    # e.g. a = INT_MAX (2^31 - 1) and b = -15 
    if (a & SIGN_MASK and not b & SIGN_MASK) or (not a & SIGN_MASK and not b & SIGN_MASK):
        if a & SIGN_MASK:
            return b
        return a
    return max_old(a, b)
