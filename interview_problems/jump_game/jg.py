

def JG(A):
    return J(A, len(A) - 1, [])

def J(A, n, M):
    if len(M) > n:
        return M[n]
    if n == 0:
        M.append(True)
        return M[n]
    for j in range(n):
        if J(A, j, M) and A[j] >= (n - j):
            return True
    return False

print JG([2,3,1,1,4])
print JG([3,2,1,0,4])
