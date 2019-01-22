# in notes

from collections import defaultdict
from itertools import product

def capture(board):
    r = len(board)
    c = len(board[0])

    seeds = [(y, 0) for y in range(r) if board[y][0] == 'O'] + \
            [(y, c-1) for y in range(r) if board[y][c-1] == 'O' ] + \
            [(0,x x) for x in range(c) if board[0][x] == 'O'] + \
            [(r-1, x) for x in range(c) if board[r-1][x] == 'O']

    marked = defaultdict(lambda: False)
    for seed in seeds:
        dfs(seed, board, marked)

    for y, x in product(range(r), range(c)):
        if not marked[y, x]:
            board[y][x] = 'X'



def dfs(loc, board, marked):
    if marked[loc]:
        return

    def valid(y, x):
        return y >= 0 and y < len(board) and x >= 0 and x < len(board[0])

    marked[loc] = True

    offsets = [(1,0),(-1,0),(0,1),(0,-1)]
    neighbors = [tuple(sum(pair) for pair in zip(off, loc)) for off in offsets]

    for n in neighbors:
        if valid(*n) and board[n[0]][n[1]] == 'O':
            dfs(n, board, marked)


board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]

capture(board)

print board
