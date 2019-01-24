"""

eight queens


we can assume that each queen gets its own row
so its really a matter of deciding the columns (this thinking can be switched WLOG)

cols = [col of each queen in each row]



[0 5 2
 ^

diagonal strike
	if col dist = row dist
	col dist is abs(cols[i] - possible_col)
	row dist is abs(i - len(cols))

if len(cols) == 8:
	return

for possible_col in range(8):
possible_col isnt in cols (vertical strike)
no diagonal strike 

"""



def diagonal_strike(cols, candidate):
	for i, c in enumerate(cols):
		col_dist = abs(c - candidate)
		row_dist = abs(i - len(cols))
		if row_dist == col_dist: return True
	return False

def nqueens(n):
	out = []
	def _nqueens(col_positions):
		if len(col_positions) == n:
			out.append(col_positions)

		for new_col_pos in range(n):
			if new_col_pos in col_positions:
				continue
			if diagonal_strike(col_positions, new_col_pos):
				continue
			_nqueens(col_positions[:] + [new_col_pos])

	_nqueens([])	
	return out
		
print nqueens(4)
