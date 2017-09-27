from math import log10

def palindrome(n):
    assert n >= 0
    def most_sig(k):
        return k / (10 ** int(log10(k)))

    def least_sig(k):
        return k % 10

    def shrink(k):
        k = k % ((10 ** int(log10(k))))
        k = k / 10
        return k

    while n > 9 and most_sig(n) == least_sig(n):
        n = shrink(n)

    return True if n < 10 else False

print palindrome(33133)
print palindrome(3223)
print palindrome(3233)
print palindrome(3)

