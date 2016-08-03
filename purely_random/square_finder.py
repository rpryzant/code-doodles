# This program comes from an interview question I got a year ago ish. It's one of my favorites.
# I answered it poorly in the actual interview. Since the interview, though, I've spent more
# and more time thinking about it. You can get some pretty beautiful solutions.
#
# Given a binary matrix, find all rectangles of ones in it.


SAME_ROW = 0
SAME_COL = 1
DIAGONAL = 2


def one_generator(matrix):
    """generates the indexes of all 1's in a matrix"""
    for i, row in enumerate(matrix):
        for j, xij in enumerate(row):
            if xij == 1:
                yield Coord((i, j))

class Coord:
    def __init__(self, coord):
        self.r, self.c = coord

    def __str__(self):
        return "(%s, %s)" % (self.r, self.c)

class SquareBuilder:
    def __init__(self, coord):
        self.num_corners = 0
        self.corners = [coord]
        self.membership_rules = [lambda x: True]
        self.pair_rule_store = {
            SAME_ROW: [lambda x: any(x.c == y.c for y in self.corners)],
            SAME_COL: [lambda x: any(x.r == y.r for y in self.corners)],
            DIAGONAL: [lambda x: x.r == self.corners[1].r and x.c == self.corners[0].c,
                       lambda x: x.r == self.corners[0].r and x.c == self.corners[1].c]
            }

    def add(self, coord):
        for rule in self.membership_rules:
            if rule(coord):
                self.corners.append(coord)
                if len(self.corners) == 2:
                    if self.corners[0].r == self.corners[1].r:
                        rule_type = SAME_ROW
                    elif self.corners[0].c == self.corners[1].c:
                        rule_type = SAME_COL
                    else:
                        rule_type = DIAGONAL
                    self.membership_rules = self.pair_rule_store[rule_type]
                elif len(self.corners) == 3:
                    self.membership_rules = [lambda x: self.pair_rule_store[SAME_ROW][0](x) and self.pair_rule_store[SAME_COL][0](x)]
                elif len(self.corners) == 4:
                    self.membership_rules = [lambda x: False]
                return True
        return False


    def is_full(self):
        return len(self.corners) == 4

    def give_square(self):
        if self.is_full():
            return self.corners
        else:
            return None

    def __str__(self):
        return ' '.join(str(c) for c in self.corners)


test = [
    [1,0,0,0,0],
    [0,1,0,1,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,1,1,0]
]


squares = []
for coord in one_generator(test):
    map(lambda x: x.add(coord), squares)
    squares.append(SquareBuilder(coord))

for square in squares:
    if square.is_full():
        print square



c1 = Coord
s = SquareBuilder(Coord((0,0)))
print s.add(Coord((1,0)))
print s.add(Coord((8,0)))
print s.add(Coord((1,1)))
print s.add(Coord((3,1)))
print s.add(Coord((0,1)))
print s.is_full()
for coord in s.give_square():
    print coord
