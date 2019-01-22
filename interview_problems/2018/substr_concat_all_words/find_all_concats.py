import re

def find(s, words):
    t = len(words[0])
    matches = []
    for word in words:
        matches += [m.start() for m in re.finditer(word, s)]
    matches = sorted(matches)
    for i in range(0, len(matches) - len(words) + 1):
        if valid(matches[i : i + len(words)], t):
            yield matches[i]

def valid(a, t):
    return all(map(lambda (x,y): y-x == t, zip([a[0]-t]+a, a)))


print [x for x in find("barfoothefoobarman", ["foo", "bar"])]
