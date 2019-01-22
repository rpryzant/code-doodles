
def count(s):
     c = 1
     out = ""
     for i in range(1, len(s)):
         if s[i] == s[i-1]:
             c += 1
         else:
             out += "%s%s" % (c, s[i-1])
             c = 1
     out += "%s%s" % (c, s[-1])
     return out

def __genN(n, S):
    if n < len(S):
        return S[n]
    if n == 0:
        S.append("1")
        return S[n]
    seed = __genN(n-1, S)
    S.append(count(seed))
    return S[n]

def genN(n):
    return __genN(n, [])


print genN(4)
