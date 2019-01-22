"""

for i, x in range(0, n + 1) with buffer of 0 in each side
    newrow[i] = r[i-1] + r[i]



"""



def gen_triangle(n):
    if n <= 0:
        return []

    out = [[1]]
    for i in range(2, n+1):
        out += [[(out[-1][j-1] if j > 0 else 0) + (out[-1][j] if j < len(out[-1]) else 0) for j in range(i)]]

    return out


print gen_triangle(1)
print gen_triangle(5)
