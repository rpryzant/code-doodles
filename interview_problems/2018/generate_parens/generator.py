
def gen_parens(n):
    strs = [('', 0, 0)]
    min_paren_count = lambda x: min(s[x] for s in strs)
    while min_paren_count(1) < n or min_paren_count(2) < n:
        ln = len(strs)
        for _ in range(ln):
            s, l, r = strs[0]
            if l < n:
                strs.append((s + '(', l+1, r))
            if r < n and r < l:
                strs.append((s + ')', l, r+1))
            strs = strs[1:]
    return [x[0] for x in strs]


def gen_parensR(n):
    a = []
    return __gen_parensR(a, "", n, n)

def __gen_parensR(a, s, l, r):
    if r == 0:
        a.append(s)
    if l > 0:
        __gen_parensR(a, s + "(", l - 1, r)
    if r > l:
        __gen_parensR(a, s + ')', l, r-1)
    return a

print gen_parens(3)
print gen_parensR(3)
