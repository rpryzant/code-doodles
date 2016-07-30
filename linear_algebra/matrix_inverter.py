# Program to calculate the determinant of a matrix
#
# Note that this does NOT use numpy ndarrays to represent matrices
#       It uses plain old 2-d python lists (first index is row, second is column)

from math import pow

def blank_copy(A):
    return [row[:] for row in A]

def swap(A, i, j):
    tmp = A[i][j]
    A[i][j] = A[j][i]
    A[j][i] = tmp

def pp(A):
    """ printpretty """
    for row in A:
        print '  '.join(str(x) for x in row)

def multiply_by_scalar(A, c):
    for i, row in enumerate(A):
        for j, col in enumerate(A[i]):
            A[i][j] *= c


def minor(A, i, j):
    """
    Returns a new matrix M which is A minus row i & col j
    """
    M = [row[:] for k, row in enumerate(A) if k != i]
    for row in M:
        del row[j]
    return M
    

def cofactor(A):
    """
    Returns the cofactor matrix of A
    Each element Cij is the determinant of A's i,jth minor multiplied by -1^{i+j}
    """
    C = blank_copy(A)
    for i, row in enumerate(C):
        for j, col in enumerate(C[i]):
            M = minor(A, i, j)
            detM = determinant(M)            
            C[i][j] = pow(-1, i+j) * detM
    return C

def transpose(A):
    n = len(A[0])
    for i, row in enumerate(A):
        for j in range(i, n):
            swap(A, i, j)


def adjoint(A):
    """
    Returns the adjoint matrix of A 
    This is the transpose of A's cofactor matrix
    """
    C = cofactor(A)
    transpose(C)
    return C


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
            B = minor(A, 0, j)
            # math.pow instead of ** because -1**0 = -1
            det += pow(-1, 0 + j) * determinant(B) * aij   
    return det


def invert(A):
    """
    Returns a new matrix that is the two-sided inverse of A
    A A^-1 = I = A^-1 A
    """
    B = blank_copy(A)
    det = determinant(B)    
    B = adjoint(B)
    multiply_by_scalar(B, 1/det)
    return B


test = [[1,2,0],[-1,1,1],[1,2,3]]
print pp(test)
print determinant(test)

print pp(cofactor(test))
print pp(invert(test))
