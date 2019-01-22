# in notes

def gen_spiral(M):
    m = len(M)
    for o in range(m/2):
        for x in gen_ring(M, o):
            yield x
    if m % 2:
        yield M[m/2][m/2]

# o = offset
def gen_ring(M, o):
    m = len(M)
    n = len(M[0])
    # top row
    for col in range(o, n - o):
        yield M[o][col]
    # right col
    for row in range(o + 1, m - o):
        yield M[row][n - o - 1]
    # bottom row
    for col in range(o, n - o - 1)[::-1]:
        yield M[m - o - 1][col]
    # left col
    for row in range(o + 1, m - o - 1)[::-1]:
        yield M[row][o]


test = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

test = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [14,15,16,17]
]

test = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

for row in test:
    print row
for x in gen_spiral(test):
    print x
