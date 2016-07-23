

def sort(a):
    return sortR(a, 0, len(a) - 1)


def sortR(a, low, high):
    if low >= high:
        return a

    mid = (low + high) / 2
    sortR(a, low, mid)
    sortR(a, mid + 1, high)
    merge(a, low, mid, high)

def merge(a, low, mid, high):
    i = low
    k = low
    j = mid + 1

    copy = [x for x in a]

    while i <= mid and j <= high:
        if copy[i] < copy[j]:
            a[k] = copy[i]
            i += 1
        else:
            a[k] = copy[j]
            j += 1
        k += 1
    
    while i <= mid:
        a[k] = copy[i]
        i += 1
        k += 1


test = [6,2,6,1,-5,9]
print test
sort(test)
print test
