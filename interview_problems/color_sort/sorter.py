# i like my solution to this one!

from collections import defaultdict


def sort(a):
    if not a:
        return []
    d = defaultdict(lambda: 0)
    for x in a:
        d[x] += 1
    return [0 for _ in range(d[0])] + [1 for _ in range(d[1])] + [2 for _ in range(d[2])]

def sort2(a):
    if not a:
        return []
    out = [[],[],[]]
    for x in a:
        out[x].append(x)
    return out[0] + out[1] + out[2]


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

# o(n) and in place!
def sort3(a):
    fp = 0
    bp = len(a) - 1
    i = 0
    while i <= bp and fp < bp:
        if a[i] == 0:
            swap(a, i, fp)
            while a[fp] == 0:
                fp += 1
        elif a[i] == 2:
            swap(a, i , bp)
            while a[bp] == 2:
                bp -= 1
        else:
            i += 1
    return a



test = [2,2,1,0,1,2,2,1,0,0,0,1,2,2,1]
print sort(test)
print sort2(test)
print test
print sort3(test)


test = [2,0,0,0,0,0]
print sort3(test)

test = [2,2,2,2,0]
print sort3(test)
