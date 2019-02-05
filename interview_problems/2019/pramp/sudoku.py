"""
given:    9x9 array   
            elements are in '1-9\.'
we want to see if the puzzle is solvable (not if SOLVED)

when is soduku solved?
  1. seperate digits in each row
  2. "" col
  3. "" each 3.3 subarray
  
when is something NOT SOLVABLE?
  if dup in row, col, or subarray (dup has to be in 1-9) . 
  

def is solvable:
  return not not_solvable(board)


1: find all dups
   ensure dup pairs are not in same row, col or subarray


=============================================
2: iterate through all rows, cols, then subarrays
      [3 5 2 6 3] (row, col, or subarray)
   make sure no repeated elements
=============================================


PSEUDOCODE

is_solvable(board):
  for row in row_iterator(board):
    if len(row) != len(set(row)):
      return False
  for col in col_iterator(board):
    if len(col) != len(set(col)):
      return False
  for subarr in subarr_iterator(board):
    if len(subarr) != len(set(subarr)):
      return False

  return True


rows: [0, ]

N = 9
O(N^2) # 
"""
def row_iterator(board):
  for row in board:
    yield [x for x in row if x != '.']

def col_iterator(board):
  for ci in range(9):
    yield [board[ri][ci] if board[ri][ci] != '.' for ri in range(9)]
  
def subarr_iterator(board):
  def get_subarr(topleft_row, topleft_col): 
    out = []
    for ri in range(3):
      for ci in range(3):
        cur_element = board[ri + topleft_row][ci + topleft_col]
        if cur_element != '.':
          out.append(cur_element)
    return out

  for ri in range(3):
    for ci in range(3):
      yield get_subarr(ri * 3, ci * 3)

      
def is_solvable(board):
  for row in row_iterator(board):
    if len(row) != len(set(row)):
      return False
  for col in col_iterator(board):
    if len(col) != len(set(col)):
      return False
  for subarr in subarr_iterator(board):
    if len(subarr) != len(set(subarr)):
      return False

  return True
