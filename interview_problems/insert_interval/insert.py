


def insert(ivals, x):
    ii = search(ivals, x)
    ivals.insert(ii, x)
    while overlap(ivals, ii) and ii < len(ivals) - 1:
        merge_adjacent(ivals, ii)
    return ivals

def overlap(ivals, i):
    return max(ivals[i][0], ivals[i+1][0]) < min(ivals[i][1], ivals[i+1][1])

def merge_adjacent(ivals, i):
    new = [min(ivals[i][0], ivals[i+1][0]), max(ivals[i][1], ivals[i+1][1])]
    del ivals[i+1]
    ivals[i] = new

def search(a, x):
    return searchR(a, x, 0, len(a) - 1)

def searchR(a, x, low, high):
    if low > high:
        return high
    mid = (low+high) / 2
    if a[mid][0] < x[0] and a[mid][1] > x[0]:
        return mid
    if a[mid][0] > x[0]:
        return searchR(a, x, low, mid - 1)
    else:
        return searchR(a, x, mid + 1, high)




test = [[1,3],[6,9]]
print insert(test, [2,5])



test = [[1,2],[3,5],[6,7],[8,10],[12,16]]
print insert(test,[4,9])

