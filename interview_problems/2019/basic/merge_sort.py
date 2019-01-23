



def merge_sort(l):
    if len(l) < 2:
        return l

    m = len(l) / 2
    first_half = merge_sort(l[:m])
    second_half = merge_sort(l[m:])

    return merge(first_half, second_half)

def merge(a, b):
    ai, bi = 0, 0
    out = []
    while ai < len(a) or bi < len(b):
        if ai == len(a):
            out.append(b[bi])
            bi += 1
        elif bi == len(b):
            out.append(a[ai])
            ai += 1
        elif a[ai] <= b[bi]:
            out.append(a[ai])
            ai += 1
        elif b[bi] <= a[ai]:
            out.append(b[bi])
            bi += 1

    return out




print merge_sort([])
print merge_sort([1])
print merge_sort([1, 1])
print merge_sort([1, 2])
print merge_sort([2, 1])
print merge_sort([2, 1, 100, 34, 6,3])
