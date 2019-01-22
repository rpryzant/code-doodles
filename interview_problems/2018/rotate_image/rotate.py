


def gen_col_from_bottom(m, c):
    for i in range(len(m))[::-1]:
        yield m[i][c]

def rotate_not_in_place(m):
    return [[xij for xij in gen_col_from_bottom(m, j)] for j in range(len(m[0]))]
    


def rotate_in_place(m):
    n = len(m)
    for i in range(n / 2):
        for j in range(i, n - i - 1):
            rotate_element(m, i, j)

def rotate_element(m, i, j):
    n = len(m) - 1
    cur = exchange(m[i][j], m, j, n-i)
    cur = exchange(cur, m, n-i, n-j)
    cur = exchange(cur, m, n-j, i)
    exchange(cur, m, i, j)

def exchange(x, m, r, c):
    t = m[r][c]
    m[r][c] = x
    return t


test = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print rotate_not_in_place(test)
print "##################"
print test
rotate_in_place(test)
print test
