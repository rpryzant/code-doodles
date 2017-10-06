"""
boom 

dfs
n!
   there's early stopping, e.g. cut it off when num chars
    dips under that of d, but doesn't help big-O
with memoization (dp)
   n^2
"""


def subsequences(s, t):
    cache = {}

    def recurse(s_part):
        if s_part in cache:
            return cache[s_part]
        if s_part == t:
            cache[s_part] = 1
            return 1
        elif len(s_part) <= len(t):
            cache[s_part] = 0
            return 0
        count = 0
        for i in range(len(s_part)):
            count += recurse(s_part[:i] + s_part[i+1:])
        cache[s_part] = count
        return count

    return recurse(s[:])

print subsequences('rabbbbbbbbbit', 'rabbit')
