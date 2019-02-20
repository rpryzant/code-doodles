"""
row_offset =
col_offset



00 01 02
10 11 12
20 21 22


ro = 0 
co = 0 

00 01 02 12 22 21 20 10

ro 1
co 1

11



input:  inputMatrix  = [ [1,    2,   3,  4,    5],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]
                 
ro 0                         
co 0

1 2 3 4 5 10 15 20 19 18 17 16 11 6

ro 1
co 1

"""

def single_spiral(m, o):
  nrows, ncols = len(m), len(m[0])
  out = []

  # right
  for x in range(o, ncols - o):
    out.append(m[o][x])

  # down
  for y in range(o + 1, nrows - o):
    out.append(m[y][ncols - 1 - o])

  # left
  for x in range(o, ncols - o - 1)[::-1]:
    out.append(m[nrows - 1 - o][x])  
  
  # up (ignore last)
  for y in range(o + 1, nrows - o - 1)[::-1]:
    out.append(m[y][o])

  return out
  

def spiral_copy(m):
  nrows, ncols = len(m), len(m[0])

  out = []
  for offset in range(min(nrows, ncols)):
    out += single_spiral(m, offset)

  return out

