"""
1) make triangle of size k
     return last row
    ======> O(k^2) space! bad

2) think
     1
    1  1
  1   2   1
1   3   3   1


2) 

0 1 2 3 4
1 1 1 1 1
2 1 2 3
3 1 3
4 1

make ^, loop through rows and throw away prev row



3) make pascals triangle, throw away rows once you don't need them
     =====> O(k) space


"""


def getKthRow(k):
    if k  < 0:
        return []
    if k == 0:
        return [1]
    out = [[1]]
    for j in range(1, k + 1):
        out += [[(out[-1][i-1] if i > 0 else 0) + (out[-1][i] if i < len(out[-1]) else 0) for i in range(j + 1)]]
        del out[0]
    return out[-1]


print getKthRow(3)
print getKthRow(2)
print getKthRow(1)
print getKthRow(0)
