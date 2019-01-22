from collections import defaultdict

def longest_substr(s):
    start = 0
    l = 0
    maxl = 0
    max_str = ''
    d = defaultdict(lambda: False)
    for i, ch in enumerate(s):
        if d[ch]:
            if l > maxl:
                max_str = s[start: i]
                maxl = l
            l = 0
            d = defaultdict(lambda: False)
            start = i
        d[ch] = True
        l += 1
    if l > maxl:
        return s[start:]
    else:
        return max_str


test = "abcabcbb"
print longest_substr(test)
test = "bbbbb"
print longest_substr(test)
test = "aaaaefg"
print longest_substr(test)
test = "abcdefg"
print longest_substr(test)
