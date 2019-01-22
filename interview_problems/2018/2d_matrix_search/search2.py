"""
(m x n)  matrix search

rows are sorted left to right
rows above are larger than rows below

1) bf:
    O(mn) try everything!

2) binary search
    locate insertion row
       = row with greatest starting value less than T
    search that row

    O(log m + log n)
    ( O(m) space because of the way i'll implement it... but could fix this)
"""
from bisect import bisect_left


def matrix_search(m, x):
    row_starts = [r[0] for r in m]
    insertion_row = bisect_left(row_starts, x) - 1
    insertion_col = bisect_left(m[insertion_row], x)
    if m[insertion_row][insertion_col] == x:
        return insertion_row, insertion_col
    return None


m = [ [1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50] ]
print matrix_search(m, 5)
print matrix_search(m, 30)
print matrix_search(m, 31)
print matrix_search(m, -1)







