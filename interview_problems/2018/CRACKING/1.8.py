

def gen_zeros(m):
    for i, row in enumerate(m):
        for j, ai in enumerate(row):
            if ai == 0:
                yield i, j

def set_row(m, row, val):
    m[row] = [val for _ in range(len(m[row]))]

def set_col(m, col, val):
    for row in m:
        row[col] = val

def zero_out(m):
    z_rows = [0 for _ in range(len(m))]
    z_cols = [0 for _ in range(len(m[0]))]
    zeros = [coord for coord in gen_zeros(m)]
    for coord in zeros:
        if not z_rows[coord[0]]:
            z_rows[coord[0]] = 1
            set_row(m, coord[0], 0)
        if not z_cols[coord[0]]:
            z_cols[coord[1]] = 1
            set_col(m, coord[1], 0)

m = [
    [1,1,1,0,1],
    [0,1,1,1,1],
    [1,1,1,1,1]
]
print m
zero_out(m)
print m
