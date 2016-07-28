import numpy as np
from matrix_utils import insert_col, insert_row, first_nonzero_in_row, first_zero_in_row, last_nonzero_in_row

class LinAlg:    

    @staticmethod
    def nullspace(A):
        """
        Given a numpy ndarray A, returns a new numpy ndarray whose columns are a basis for the nullspace of A
        """
        U, pivots = LinAlg.echelon_form(A, save_pivots = True)

        m, n = U.shape
        N = None
        pivot_columns = [p[1] for i, p in enumerate(pivots)]
        free_columns = list(set(range(n)) - set(pivot_columns))
        # use each free variable (/column) to make an independant nullspace vector
        for col in free_columns:
            x = np.zeros(n)
            # take 1 of this free column
            x[col] = 1
            # find the last nonzero element (it might have a bunch of 0s at the bottom since U is upper triangular)
            starting_row = last_nonzero_in_row(U[:,col])
            # work up through the free col, finding and remembering how much of the pivot cols you need to knock out each ith element
            for i in range(starting_row + 1)[::-1]:
                pivot = next((p for p in pivots if p[0] == i), None)
                multiplier = -U[i, col] / U[pivot]
                U[:,col] += U[:,pivot[1]] * multiplier
                x[pivot[1]] = multiplier
            N = insert_col(N, x)
        return N


    @staticmethod
    def echelon_form(A, save_pivots = False):
        """ 
        Given a numpy array A, returns it's upper-triangular echelon form U via Gaussian elimination
        Optionally saves the locations of the pivots into a list of coordinate tuples
        """
        m, n = A.shape
        A = A.astype(float)
        current_row = 0
        pivots = []
        # try to find pivots in each column
        for current_col in range(n):
            # stop if you've found pivots in each row
            if current_row == m:
                break
            # continue onto next column if this one is all zero's
            if np.all(A[current_row:,current_col] == 0):
                continue   # continuation implies matrix is singular b/c not full rank

            # do a row exchange if pivot is 0 (we know there's at least 1 nonzero below it)
            if A[current_row, current_col] == 0:
                rest_of_column = A[current_row:, current_col] 
                exchange_row = first_nonzero_in_row(rest_of_column) + current_row
                A[[current_row, exchange_row]] = A[[exchange_row, current_row]]

            # remember pivot for this column            
            pivot = A[current_row, current_col]
            if save_pivots:
                pivots.append((current_row, current_col))

            # clear out everything below the pivot
            for row_index in range(current_row + 1, m):
                if A[row_index, current_col] != 0:
                    multiplyer = A[row_index, current_col] / pivot
                    A[row_index] -= multiplyer * A[current_row]
            current_row += 1

        if save_pivots:
            return A, pivots
        return A


def run_tests():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    LinAlg.echelon_form(A)

    B = np.array([[1,2,2,2],[2,4,6,8],[3,6,8,10]])
    LinAlg.echelon_form(B)
    LinAlg.nullspace(B)

    C = np.array([[0,4,1], [1,2,1], [3,8,1]])
    LinAlg.echelon_form(C)

if __name__ == "__main__":
    run_tests()
