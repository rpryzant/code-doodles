

def coins(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return coins(n-25) + coins(n-10) + coins(n-5) + coins(n-1)

def coins2(n):
    return coinsR(n, [-1 for _ in range(n+1)])

def coinsR(n, m):
    if n < 0:
        return 0
    elif n == 0:
        m[0] = 1
        return 1
    elif m[n] > -1:
        return m[n]
    else:
        m[n] = coinsR(n-25, m) + coinsR(n-10, m) + coinsR(n-5, m) + coinsR(n-1, m)
        return m[n]



def coins3(n):
    M = []
    for np in range(n+1):
        if np == 0:
            M.append(0)
        else:
            counts = get_counts([1,5,10,25], np, M)
            M.append(min(counts) + 1)
    return M[-1]


def get_counts(denoms, np, M):
    return [M[np - x] for x in filter(lambda y: y <= np, denoms)]


print coins(7)
print coins2(73)
print coins3(73)
