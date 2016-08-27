

class Listy:
    def __init__(self, l):
        self.list = l

    def elementAt(self, i):
        try:
            return self.list[i]
        except IndexError:
            return -1


START_EDGE = 5


def searchR(a, l, h, t, starth):
    if l > h:
        if h == starth:
            return searchR(a, l, h*2, t, h*2)
        return -1
    m = (l + h)/2
    if a.elementAt(m) == t:
        return m
    elif a.elementAt(m) > t or a.elementAt(m) == -1:
        return searchR(a, l, m-1, t, starth)
    else:
        return searchR(a, m+1, h, t, starth)


def search(a, t):
    return searchR(a, 0, START_EDGE, t, START_EDGE)


l = Listy([1,2,3,4,6,7, 9, 10])
print search(l, 4)
print search(l, 15)
print search(l, 5)
print search(l, 10)

l = Listy([1,2])
print search(l, 2)
