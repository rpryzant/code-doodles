# naive soln
# enumerate all substrs, get palinness and len
# O(n^3)
def is_palindrome(s):
    if not s or len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[0:-1])

def gen_substrs(s):
    for i in range(len(s)):
        for j in range(i, len(s)):
            yeild s[i:j]

def longest_palindromic_substr(s):
    maxlen = 0
    max = None
    for substr in gen_substrs(s):
        if is_palindrome(substr) and len(substr) > maxlen:
            maxlen = len(s)
            max = substr
    return max




############# FASTER WAY OF DOING THINGS
# blast-like match expansion for each elment
# O(n^2)
def fast_LPS(s):
    maxlen = 0
    max = None
    for pivot in range(len(s)):
        lb, ub = extend(pivot, s)
        if ub - lb > maxlen:
            maxlen = ub - lb
            max = s[lb:ub+1]
    return max

def def extend(p, s):
    lb = ub = p
    while (lb >= 0) and (ub < len(s)) and (s[lb] == s[ub]):
        lb -= 1
        ub += 1
    return lb+1, ub-1
