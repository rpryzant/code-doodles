



def search(M, w):
    if not w or not M:
        return False

    candidates = [(r, c, 1) for r, row in enumerate(M) for c, ch in enumerate(row) if ch == w[0]]
    visited = []



    while len(candidates) > 0:
        coord = candidates.pop()

        if not (coord[0], coord[1]) in visited:
            if coord[2] == len(w):
                return True

            if coord[0] > 0 and M[coord[0] - 1][coord[1]] == w[coord[2]]:
                candidates.append((coord[0] - 1, coord[1], coord[2] + 1))
            elif coord[0] < len(M) - 1 and M[coord[0] + 1][coord[1]] == w[coord[2]]:
                candidates.append((coord[0] + 1, coord[1], coord[2] + 1))
            elif coord[1] > 0 and M[coord[0]][coord[1] - 1] == w[coord[2]]:
                candidates.append((coord[0], coord[1] - 1, coord[2] + 1))
            elif coord[1] < len(M[0]) - 1 and M[coord[0]][coord[1] + 1] == w[coord[2]]:
                candidates.append((coord[0], coord[1] + 1, coord[2] + 1))

            visited.append((coord[0], coord[1]))

    return False




test = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

print 'ABCCS'

for l in test:
    print l

print search(test, 'ABCCS')
print search(test, 'ASFB')
print search(test, 'ASAA')
print search(test, '')
