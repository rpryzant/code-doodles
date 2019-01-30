"""tic tac win

see if someone won a game of tic tac toe
win if 
diagonal
horizontal
vertical
is all same type (X, O)

3x3 array with string values (X, O, N)

8 “lines”

check each

00  02
  11
20  22
"""


def gen_diags(board):
    n = len(board)
    yield [board[i][j] for i, j in zip(range(n), range(n))]

    yield [board[i][j] for i, j in zip(range(n), range(n)[::-1])]




def has_won(board):

    def is_row_win(pos):
        return len(set([board[r][pos] for r in range(3)])) == 1 \
            and board[pos][pos] in [‘O’, ‘N’]
    def is_col_win(pos):
        return len(set([board[pos][c] for c in range(3)])) == 1 \
            and board[pos][pos] in [‘O’, ‘N’]

    # check rows + cols
    for position in range(3):
        if is_row_win(position) or is_col_win(position):
            return board[position][position]

    # check forward diag
    if len(set([board[i][i] for i in range(3)])) == 1 \
            and board[0][0] in [‘O’, ‘N’]:
        return board[0][0]

    # check backward diag
    if len(set([board[1+i][1-i] for i in range(-1, 1)])) == 1 \
            and board[1][1] in [‘O’, ‘N’]:
        return board[1][1]

    return None

