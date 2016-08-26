

def isMatch(a, b):
    bi = 0
    bl = len(b) - 1
    for i in range(len(a)):
        if  (bi > bl) or (a[i] != b[bi] and b[bi] != '?' and b[bi] != '*'):
            return False
        elif (b[bi] == '*' and b[min(bi+1, bl)] == a[i]) or b[bi] == a[i]:
            bi += 1
    return True


print isMatch("aa","a"), "false"
print isMatch("aa","*"), "true"
print isMatch("","*"), "true"
print isMatch("aa","aa"), "true"
print isMatch("aaa","aa"), "false"
print isMatch("aa", "*"), "true"
print isMatch("aa", "a*"), "true"
print isMatch("ab", "?*"), "true"
print isMatch("aab", "c*a*b"), "false"
