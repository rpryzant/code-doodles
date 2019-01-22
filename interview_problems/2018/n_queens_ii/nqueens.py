# wanted to solve it on my own because i looked online the first time

def count_nqueens(n):
    return c_nqueensR(n, [])

def c_nqueensR(n, cols):
    if len(cols) == n:
        return 1
    sum = 0
    for i in range(n):
        if valid(i, cols):
            cols.append(i)
            sum += c_nqueensR(n, cols)
            cols.pop()
    return sum

def nqueens(n):
    result = []
    nqueensR(n, [], result)
    return result

def nqueensR(n, cols, result):
    if len(cols) == n:
        result.append(drawboard(n, cols))
    for i in range(n):
        if valid(i, cols):
            cols.append(i)
            nqueensR(n, cols, result)
            cols.pop()

def valid(newcol, cols):
    newrow = len(cols)
    for row, col in enumerate(cols):
        if newcol == col:
            return False
        if newcol + newrow == row + col:
            return False
        if newrow - newcol == row - col:
            return False
    return True

def drawboard(n, cols):
    s = []
    for col in cols:
        s.append( ('.' * col) + 'Q' + ('.' * (n - col - 1)) )
    return s

print nqueens(4)
print count_nqueens(4)
print count_nqueens(8)
