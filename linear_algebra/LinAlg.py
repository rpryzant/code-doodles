import numpy as np

class LinAlg:
    

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

            # do a row exchange and re-retrieve if pivot is 0 (we know there's at least 1 nonzero below it)
            if A[current_row, current_col] == 0:
                rest_of_column = A[current_row:, current_col] 
                exchange_row = next((i for i, x in enumerate(rest_of_column) if x > 0), None)
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

    C = np.array([[0,4,1], [1,2,1], [3,8,1]])
    LinAlg.echelon_form(C)

if __name__ == "__main__":
    run_tests()
