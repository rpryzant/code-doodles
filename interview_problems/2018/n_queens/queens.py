

def draw_board(cols, n):
    out = []
    for col in cols:
        out.append( ('.' * (col - 1)) + 'Q' + ('.' * (n - col)) )
    return out

def valid(col, cols):
    # you know the row is new so no hit there
    row = len(cols)
    for r, c in enumerate(cols):
        # same col
        if col == c:
            return False
        # up diagonal
        if row + col == r + c:
            return False
        # down diagonal
        if row - col == r - c:
            return False
    return True

def queensR(result, cols, n):
    if len(cols) == n:
        result.append(draw_board(cols, n))
        return
    for i in range(n):
        if not valid(i, cols):
            continue
        cols.append(i)
        queensR(result, cols, n)
        cols.pop()

def queens(n):
    if n <= 0:
        return
    result = []
    queensR(result, [], n)
    return result

print queens(4)
