
FOUND_ELEMENT = -1


def find(M, x):
    if not M:
        return False
    r = find_row(M, x)
    if r == FOUND_ELEMENT:
        return True
    elif r < len(M):
        return find_col(M[r], x)
    return False


def find_row(M, x):
    return frR(M, x, 0, len(M) - 1)

def frR(M, x, l, h):
    if l > h:
        return l
    m = (l + h) / 2
    if x == M[m][-1]:
        return FOUND_ELEMENT
    elif x < M[m][-1]:
        return frR(M, x, l, m-1)
    else:
        return frR(M, x, m+1, h)

def find_col(R, x):
    return fcR(R, x, 0, len(R) - 1)

def fcR(R, x, l, h):
    if l > h:
        return False
    m = (l + h) / 2
    if R[m] == x:
        return True
    elif x > R[m]:
        return fcR(R, x, m+1, h)
    else:
        return fcR(R, x, l, m-1)

test = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,50]
]
    

print find(test, 3)
print find(test, 34)
print find(test, 50)
print find(test, 51)
print find(test, 15)
print find(test, -1)
