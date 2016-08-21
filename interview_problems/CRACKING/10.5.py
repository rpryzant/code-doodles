


def get_nearest_blank(a, mid):
    l = mid - 1
    h = mid + 1
    while l >= 0 and h < len(a):
        if l >= 0 and a[l] is not "":
            return l
        if h < len(a) and a[h] is not "":
            return h
        l -= 1
        h -= 1
    return -1

def find(a, s):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) / 2
        if not a[mid]:
            mid = get_nearest_blank(a, mid)
            if mid == -1:
                return -1
        print s < a[mid]
        if s < a[mid]:
            high = mid - 1
        elif s > a[mid]:
            low = mid + 1
        else:
            return mid

test = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]

print find(test, "ball")
print find(test, "dad")
