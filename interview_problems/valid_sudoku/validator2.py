#instead of asking if valid solution, asks if board is *solvable*




from collections import defaultdict

def check_for_dups(group):
      d = defaultdict(int)
      for num in group:
         if num > 0:
             d[num] += 1
             if d[num] > 1:
                 return True
      return False           

def get_cols(board):
   out = []
   for col in range(9):
       out.append([board[row][col] for row in range(9)])
   return out

def get_subgrids(board):
   out = []
   for sg_o_col in range(9)[::3]:
      for sg_o_row in range(9)[::3]:
         subgrid_elements = []
         for col_offset in range(3):
            for row_offest in range(3):
               subgrid_elements.append(board[sg_o_row + row_offest][sg_o_col + col_offset])
         out.append(subgrid_elements)
   return out
   
   
def isSolvable(board):
   # examine rows
   if all(lambda x: check_for_dups(x), board + get_cols(board) + set_subgrids(board)):
      return True
   return False
   
   
   
