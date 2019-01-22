"""
in place?

if one elem in an nxn matrix is 0, whole row and col are 0

bf: 
  1) loop through matrix
  2) if find 0 elem, set row & col to 0
  O(n^2*2n) = O(n^3)


better: cache rows & cols we've set already, 
          don't try and reset things we've done already
       O(n^2) time
       O(n) space
       short circuit by row


work on space?
  use bit vector instead of hashtable for cache (2^5x smaller)
"""

def zero_out(m):
    assert len(m) == len(m[0])
    n = len(m)
    out = []
    zero_rows, zero_cols = set(), set()
    for r in range(n):
        new_row = []
        for c in range(n):
            if m[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
                new_row.append(0)
                new_row[:c] = [0 for _ in range(c)]
            elif r in zero_rows or c in zero_cols:
                new_row.append(0)
            else:
                new_row.append(m[r][c])
        out.append(new_row)
    return out

00


test = [
    [0,1,3,4],
    [0,2,4,0],
    [3,2,4,-4],
    [3,2,0,4]]

for r in test:
    print r

print
for r in zero_out(test):
    print r
