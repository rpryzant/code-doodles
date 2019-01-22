

def compress(s):
    if not s:
        return s
    s = s.lower()
    i = 0
    out = ''
    while i < len(s) - 1:
        j = next_edge(s, i)
        out += "%s%s" % (s[i], j - i)
        i = j
    return out if len(out) < len(s) else s

def next_edge(s, i):
    try:
        return next( (j+i for j, y in enumerate(s[i:]) if y != s[i]) ) 
    except StopIteration:
        return len(s)


print compress("aaaaaa")

print compress("aabcccccaaa")
