"""
queens can attack iff:
  1) same row 
  2) same col
  3) diagonal
      queen 1 is x
      queen 2 is y

      down diag: y_r - x_r == y_c - x_c
      up diag: same? (look into)

algo:
  for row r
       try placement in (r,0) (recursively continue)
       if placement worked, save it
  return placements


FUCK yeah!!

"""
import copy




def nQueens(n):
    assert n > 0
    solutions = []

    def can_place(sofar, r, c):
        valid = lambda p1, p2: \
            (abs(p2[0] - p1[0]) != abs(p2[1] - p1[1])) and \
            (p2[0] != p1[0]) and (p2[1] != p1[1])
        return all([valid(pi, (r, c)) for pi in sofar])


    def recurse(sofar, remaining_rows):
        if remaining_rows == 0:
            solutions.append(copy.copy(sofar))
            return

        for col in range(n):
            if can_place(sofar, n - remaining_rows, col):
                sofar.add( (n - remaining_rows, col) )
                recurse(sofar, remaining_rows - 1)
                sofar.remove( (n - remaining_rows, col) )
    
    recurse(set(), n)
    return solutions

print nQueens(4)
