

def paint(I, r, c, x):
    color(I, r, c, I[r][c], x)

def color(I, r, c, x, xn):
    if r < 0 or r >= len(I) or c < 0 or c >= len(I[0]) or I[r][c] != x or x == xn:
        return

    I[r][c] = xn
    color(I, r-1, c, x, xn)
    color(I, r-1, c+1, x, xn)
    color(I, r, c+1, x, xn)
    color(I, r+1, c+1, x, xn)
    color(I, r+1, c, x, xn)
    color(I, r+1, c-1, x, xn)
    color(I, r, c-1, x, xn)
    color(I, r-1, c-1, x, xn)


test = [
[0,0,0,0,0,0,0,0],
[0,0,1,1,1,0,0,0],
[0,0,0,0,1,1,0,0],
[0,0,0,1,1,1,0,0],
[0,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,0],
[0,1,0,0,0,0,1,0],
[0,0,0,0,0,0,0,0],
]



paint(test, 1, 2, 5)

for r in test:
    print r
