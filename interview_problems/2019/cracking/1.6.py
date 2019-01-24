"""
take a string, return letters followed by their counts
return original string if len(compression) >= len(original)
input matches [A-Za-z]+

guarenteed non-zero input?



pseudocode

aabccccdee
012345678910  
"""

def iter_chunks(s):
    i = 0
    while i < len(s):
        try:
            j = next( (x+i+1 for x in range(len(s[i+1:])) if s[x+i+1] != s[i]) )
        except StopIteration:
            j = len(s)
        yield s[i: j]
        i = j

def compress(s):
    out = ''
    i = 0
    for chunk in iter_chunks(s):
        out += chunk[0] + str(len(chunk))

    if len(out) < len(s):
        return out
    return s

print compress('aabccccdee')
print compress('aabccccdeef')
print compress('aaccccee')
