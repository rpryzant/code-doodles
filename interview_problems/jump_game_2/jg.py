

def __jg(a, i, M):
    if i == 0 and not M:
        M.append(0)
        return M[i]
    elif i < len(M):
        return M[i]
    else:
        M.append(min(__jg(a, j, M) for j in range(i) if j + a[j] >= i) + 1)
        return M[i]

def jg(a):
    return __jg(a, len(a) - 1, [])




print jg([2,3,1,1,4])
