BIG = 100000000000


def min_coins(k, coins):
    return mcr(k, coins, [None for _ in range(k)])

def mcr(k, coins, M):
    if k < 0:
        return BIG
    if k == 0:
        return 0
    if M[k-1] is not None:
        return M[k-1]
    M[k-1] = min(mcr(k-c, coins, M) for c in coins) + 1
    return M[k-1]


print min_coins(7, [100,50,25,10,5,1])
print min_coins(13, [100,50,25,10,5,1])
print min_coins(15, [100,50,25,10,5,1])
