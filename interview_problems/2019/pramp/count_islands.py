"""ISLAND COUNT


thinking
given 2d binary arr
find number of islands of 1s 
	island = contiguous region of 1s, diags dont count
	islands dont streatch around sides

arr = R x C
	fewest islands = 0 or 1
	most islands = something about dividing by 2 (every other spot) 

cases:
	empty arr
	all 1s
	no 1s
	ragged (assume not)

ideas

1: aux array, every time you place a 1 without neighbors increase island count       1   1
	BAD!    11

2: aux array, every time you hit a 1 that isnt already in the aux array fill out the whole island in aux array and incrase counter

	O( RC ) O( RC ) space

pseudocode

if out of bounds
	return
elif arr[ri][ci] == 0:
	return
elif aux[ri][ci] == 0:
	aux[ri][ci] == 1
	check north, south, east, west
else:
	return 



for ri in rows
	for ci in cols
		if arr[ri][ci] == 1 and aux[ri][ci] == 0
			islands += 1
			fill_island(arr, aux, ri, ci)

return islands
"""
def check_islands(arr):
	R, C = len(arr), len(arr[0])

	def fill_island(i, j):
		if i < 0 or i >= R:   return
		elif j < 0 or j >= C: return
		elif arr[i][j] == 0:  return
		elif aux[i][j] == 1:  return
		else:
			aux[i][j] = 1
			fill_island(i+1, j)
			fill_island(i-1, j)
			fill_island(i, j+1)
			fill_island(i, j-1)

	islands = 0
	aux = [[0] * C] * R

	for ri in range(R):
		for ci in range(C):
			if arr[ri][ci] == 1 and aux[ri][ci] == 0:
				islands += 1
				fill_island(ri, ci)

	return islands

binaryMatrix =         [ [0,    1,    0,    1,    0],
                         [0,    0,    1,    1,    1],
                         [1,    0,    0,    1,    0],
                         [0,    1,    1,    0,    0],
                         [1,    0,    1,    0,    1] ]
                         
                         
print check_islands(binaryMatrix)
                         
                         
