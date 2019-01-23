
def all_perms(seq):
    out = []
    def _apr(s, r):
        if not s:
            out.append(r)
        for i in range(len(s)):
            _apr(s[:i] + s[i+1:], r + s[i])

    _apr(seq, '')
    return out

print all_perms('123')
