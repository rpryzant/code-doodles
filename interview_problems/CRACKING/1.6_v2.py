"""
string compression

aabcccccaaa
   3    4

a2b1c5a3

but return original if not smaller

FORMALLY
take a string s, and convert into
... [char][# repeats] ...

empty string? none
are capitals and lowercase the same?  no

can i pretend '...' += 'test' is O(n)?

i = 0
while i < len(s):
   get last occurance of s[i] (j)
   add s[i] + (j - i) to outgoing
   set i = j + 1
"""

def compress(s):
    assert len(s) > 0

    def next_edge(i):
        try:
            return next( (j+i+1 for j, x in enumerate(s[i+1:]) if x != s[i] ) )
        except StopIteration:
            return len(s) + 1

    out = []
    i = 0
    while i < len(s):
        j = next_edge(i)
        out += [s[i], str(j - i)]
        i = j

    compressed = ''.join(out)
    return compressed if len(compressed) < len(s) else s


print compress("aaaaaa")
print compress("aabcccccaaa")
