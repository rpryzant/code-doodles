


def merge_ivals(ivals):
    ivals = sorted(ivals, key = lambda x: x[0])
    i = 0
    while i < len(ivals) - 1:
        if max(ivals[i][0], ivals[i+1][0]) < min(ivals[i][1], ivals[i+1][1]):
            merge(ivals, i)
        else:
            i += 1
    return ivals


# pre: i < len(a) - 1
# merges a[i] with a[i+1]
def merge(a, i):
    new = [min(a[i][0], a[i+1][0]), max(a[i][1], a[i+1][1])]
    del a[i]
    del a[i]
    a.insert(i, new)


print merge_ivals([[1,3],[2,6],[8,10],[15,18]])
