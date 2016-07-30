# Program to calculate the determinant of a matrix
#
# Note that this does NOT use numpy ndarrays to represent matrices
#       It uses plain old 2-d python lists (first index is row, second is column)
#
# TODO:  pseudoinverse. import from the nullspace calculator to get row, col rank

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


def col_generator(A):
    i = 0
    while i < len(A[0]):
        yield i, [A[r][i] for r, x in enumerate(A)]
        i += 1

def dot_product(a, b):
    return sum(map(lambda (x,y): x*y, zip(a,b)))


def matrix_multiply(A, B):
    """
    Returns C = AB
    """
    m = len(A)
    n = len(B[0])
    C = [[0 for _ in range(n)] for _ in range(m)]
    for i, row in enumerate(A):
        for j, col in col_generator(B):
            C[i][j] = dot_product(row, col)
    return C

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
    At = blank_copy(A)
    n = len(A[0])
    for i, row in enumerate(At):
        for j in range(i, n):
            swap(At, i, j)
    return At

def adjoint(A):
    """
    Returns the adjoint matrix of A 
    This is the transpose of A's cofactor matrix
    """
    return transpose(cofactor(A))


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


def left_inverse(A):
    """
    Returns Aleft, the left inverse of A. Aleft = (A^t A)^-1 A^t
    Aleft A = I
    """
    AtA = matrix_multiply(transpose(A), A)
    AtAinv = inverse(AtA)
    return matrix_multiply(AtAinv, transpose(A))


def right_inverse(A):
    """
    Returns  Aright, the right inverse of A. Aright = A^t (A A^t)^-1
    A Aright = I
    """
    AAt = matrix_multiply(A, transpose(A))
    AAtInv = inverse(AAt)
    return matrix_multiply(transpose(A), AAtInv)


def pseudoinverse(A):
    #TODO
    return None



test = [[1,2,0],[-1,1,1],[1,2,3]]
print pp(test)
print determinant(test)

print pp(cofactor(test))
print pp(invert(test))


t1 = [[1,2],[3,4]]
t2 = [[2,0],[1,2]]
print pp(matrix_multiply(t1, t2))
