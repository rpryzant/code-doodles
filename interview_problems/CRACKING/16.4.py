

def gen_cols(board):
    n = len(board) 
    for i in range(n):
        yield [board[i][j] for j in range(n)]


def gen_diags(board):
    n = len(board)
    yield [board[i][j] for i, j in zip(range(n), range(n))]

    yield [board[i][j] for i, j in zip(range(n), range(n)[::-1])]


def has_won(board, t):
    n = len(board)
    # check rows
    if not all([filter(lambda x: x != t, row) for row in board]):
        return True

    # check cols
    if not all([filter(lambda x: x != t, row) for col in gen_cols(board)]):
        return True

     # check diags
    if not all([filter(lambda x: x != t, diag) for diag in gen_diags(board)]):
        return True

    return False




test = [
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11],
    [12,13,14,15]
]

print has_won(test, 0)

test = [
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0]
]

print has_won(test, 0)
