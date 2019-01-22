

def min_path(A):
    return mp(A, [[-1 for _ in range(len(A[0]))] for _ in range(len(A))], len(A)-1, len(A[0])-1)

def mp(A, S, i, j):
    if S[i][j] > -1:
        return S[i][j]
    elif i == 0 and j == 0:
        S[i][j] = A[i][j]
        return S[i][j]
    elif i == 0:
        S[i][j] = mp(A, S, i, j-1) + A[i][j]
        return S[i][j]
    elif j == 0:
        S[i][j] = mp(A, S, i-1, j) + A[i][j]
        return S[i][j]
    else:
        S[i][j] = min(mp(A, S, i-1, j), mp(A, S, i, j-1)) + A[i][j]
        return S[i][j]



test = [
    [1, 3, 2],
    [2, 1, 4],
    [1, 1, 1]
]        


print min_path(test)
