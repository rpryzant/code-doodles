# i like my solution to this! i think it's very elegant and compact



def fill_spiral(n):
    M = [[0 for _ in range(n)] for _ in range(n)]
    o = i = 0
    r = range(1, n**2 + 1)
    for j in range(n)[::-2]:
        if j == 0:                        # place middle element
            M[len(M)/2][len(M)/2] = r[-1]
        else:                             # place ring
            M = place_ring(r[i : i+ (j*4)], o, M)
            o += 1
            i = j * 4
    return M

def place_ring(span, o, M):
    n = len(M) - 1
    l = len(span) / 4
    j = 0
    for i in range(l):
        M[o][o+i] = span[j]                # top
        M[o+i][n-o] = span[j+l]            # right
        M[n-o][n-o-i] = span[j + (2*l)]    # bottom
        M[n-o-i][o] = span[j+ (3*l)]       # left
        j += 1
    return M


print fill_spiral(3)
print fill_spiral(4)
print fill_spiral(5)
