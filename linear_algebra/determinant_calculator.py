# Program to calculate the determinant of a matrix
#
# Note that this does NOT use numpy ndarrays to represent matrices
#       It uses plain old 2-d python lists (first index is row, second is column)

from math import pow

def submatrix(A, i, j):
    """
    Returns a new matrix M which is A minus row i & col j
    """
    M = [row[:] for k, row in enumerate(A) if k != i]
    for row in M:
        del row[j]
    return M
    

def determinant(A, n = None):
    """
    Calculates the determinant of a square matrix
    """
    if not n:
        n = len(A)
    det = 0

    if n < 1:
        return None
    elif n == 1:
        return A[0][0]
    elif n == 2:
        det = A[0][0] * A[1][1] - A[1][0] * A[0][1]
    else:
        # nxn matrix => det(A) = alternating sum of a column or rows' entries and their cofactors.
        #               the cofactor of an entry a_ij is det(A) without the ith row and jth column
        det = 0
        for j in range(n):
            aij = A[0][j]
            C = submatrix(A, 0, j)
            # math.pow instead of ** because -1**0 = -1
            det += pow(-1, 0 + j) * determinant(C) * aij   
    return det





test = [[1,2,0],[-1,1,1],[1,2,3]]
print determinant(test)
