# in notes

import re


TOKEN_PATTERN = "\/(\w+|\.\.)"


def simplify(path):
    tokens = re.findall(TOKEN_PATTERN, path)
    s = []
    for t in tokens:
        if t == ".." and len(s) > 0:
            s.pop()
        elif t != "..":
            s.append(t)
    return "/" + '/'.join(x for x in s)


print simplify("/home/")
print simplify("/a/./b/../../c/")
print simplify("//")
print simplify("..")
print simplify("/../")
