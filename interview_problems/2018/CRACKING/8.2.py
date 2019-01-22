
def find_path(m):
    return find_pathR(m, 0, 0, [])


def find_pathR(m, r, c, sofar):
    if r >= len(m[0]) or c >= len(m) or m[r][c] == 1:
        return
    sofar.append((r, c))
    if r == len(m[0]) - 1 and c == len(m) - 1:
        return sofar
    path_right = find_pathR(m, r+1, c, sofar[:])
    path_left = find_pathR(m, r, c+1, sofar[:])
    return path_right or path_left

test = [
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 0]
]

print find_path(test)
