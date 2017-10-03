

def smallest_diff(A, B):
    A = sorted(A)
    B = sorted(B)
    ai = bi = 0
    min = None
    while ai < len(A) - 1 and bi < len(B) - 1:
        if not min or abs(A[ai] - B[bi]) < abs(min[0] - min[1]):
            min = A[ai], B[bi]
        if ai < len(A) - 1 and A[ai] <= B[bi]:
            ai += 1
        elif bi < len(B) - 1:
            bi += 1
    return min



# 2017 version
# not happy!!
def smallestDiff(a, b):
    a = sorted(a)
    b = sorted(b)
    ai, bi = 0, 0
    min = None
    while ai < len(a) and bi < len(b):
        if not min or abs(a[ai] - b[bi]) < abs(min[0] - min[1]):
            min = a[ai], b[bi]
        if ai < len(a) and bi < len(b):
            ai += 1
        else: 
            bi += 1
    return min



print smallest_diff([1,3,15,11,2],[23,127,235,19,8])
