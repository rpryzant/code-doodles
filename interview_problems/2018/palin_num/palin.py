from math import log10, pow, floor


def digit_from_left(x, l, offset):
    return floor((x / pow(10, l - offset)) % 10)

def digit_from_right(x, offset):
    return floor((x / pow(10, offset)) % 10)

def palindrome(x):
    if x < 0:
        return False
    l = floor(log10(x))
    rO = lO = 0
    while (rO + lO) < l:
        left = digit_from_left(x, l, lO)
        right = digit_from_right(x, rO)
        if left != right:
            return False
        rO, lO = map(lambda x: x + 1, [rO, lO])
    return True

print palindrome(33133)
print palindrome(3223)
print palindrome(3233)
print palindrome(3)
