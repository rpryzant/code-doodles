

class Point:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        
    def equals(self, other):
        return self.r == other.r and self.c == other.c

class Square:
    def __init__(self, a, b):
        self.corners = [a, b, Point(a.r, b.c), Point(b.r, a.c)]

    def hash(self):
        return hash(tuple(sorted(map(lambda x: x.r, self.corners) + map(lambda x: x.c, self.corners))))

    def __str__(self):
        return ' , '.join("(%s,%s)" % (x.r, x.c) for x in self.corners)

def find_squares(M):
    d = {}
    out = []
    for p1 in gen_ones(M):
        for p2 in gen_ones(M):
            if p1.equals(p2):
                continue
            s = Square(p1, p2)
            if is_square(M, p1, p2) and not d.get(s.hash(), False):
                yield s
                d[s.hash()] = True

def gen_ones(M):
    for r, row in enumerate(M):
        for c, x in enumerate(row):
            if x == 1:
                yield Point(r, c)


def is_square(M, a, b):
    return all([M[a.r][a.c], M[b.r][b.c], M[a.r][b.c], M[b.r][a.c]]) and a.r != b.r and a.c != b.c



test = [
    [1,0,0,0,0],
    [0,1,0,1,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,1,1,0]
]

for l in test:
    print l


for s in find_squares(test):
    print s
