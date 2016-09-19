
EPSILON = 1e-5


def sqrt(x):
    low = 0.0
    high = x * 1.0
    while low <= high:
        mid = (low + high) / 2
        sq = mid * mid
        if abs(sq - x) < EPSILON:
            return mid
        elif sq > x:
            high = mid
        else:
            low = mid
    return -1


print sqrt(16)
print sqrt(15)
