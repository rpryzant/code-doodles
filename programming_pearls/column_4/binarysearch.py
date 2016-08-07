
def search(a, x):
    return __search(a, x, 0, len(a) - 1)


def __search(a, x, low, high):
    if low > high:
        return -1
    mid = (low + high) / 2
    if a[mid] == x:
        return mid
    if a[mid] > x:
        return __search(a, x, mid + 1, high)
    else:
        return __search(a, x, low, mid - 1)

l = [1,4,6,9]
print search(l, 4)
print search(l, 5)
