# i like my solution to this one!


def maximal_rectangle(M):
    multiplyer = 1
    mx = -1
    rows = M
    for _ in range(len(M)):
        max_itr = get_max(rows, multiplyer)
        mx = mx if mx > max_itr else max_itr
        rows = and_rows(rows)
        multiplyer += 1
    return mx


def get_max(rows, m):
    mx = -1
    for row in rows:
        c = 0
        for i in range(len(row)):
            if row[i]:
                c += 1
            else:
                tmp = c * m
                mx = tmp if tmp > mx else mx
                c = 0
        tmp = c * m
        mx = tmp if tmp > mx else mx        
    return mx


def and_rows(rows):
    out = []
    for i in range(len(rows) - 1):
        tmp = []
        for j in range(len(rows[i])):
            if rows[i][j] and rows[i+1][j]:
                tmp.append(1)
            else:
                tmp.append(0)
        out.append(tmp)
    return out





test = [
[1, 0, 1, 0, 0],
[1, 0, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 0, 0, 1, 0]
]

print maximal_rectangle(test)
