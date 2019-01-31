"""SUB SORT


1 2 4 [7 10 11 7 12 6 7] 16 19

find i, j such that if you sorted a[i: j+1], a would be sorted (increasing order)

arr = [a b c], where
	a is sorted
	c is sorted
	b is not sorted
	
max(a) < min(b + c)
max(a + b) < min(c)

edge cases
	sorted
	need to sort the whole thing
	size 2, 1, 0

7 2 3 4 5 6 1
a           c






better than provided solution! O(m) and accounts for bug like above: 7 8 9 6 5 4

"""

def find_limits(arr):
	mid = len(arr) // 2
	ai = mid
	ci = mid + 1
	a_max, a_min = max(arr[:ai + 1]), min(arr[:ai + 1])
	c_max, c_min = max(arr[ci:]), min(arr[ci:])
	b_max, b_min = a_max, c_min

	while a_max > min(c_min, b_min) or max(a_max, b_max) > c_min:
		# move LHS edge out
		if a_max > min(c_min, b_min) and ai > 0:
			b_min, b_max = min(b_min, arr[ai]), max(b_max, arr[ai])
			ai -= 1
			a_max = max(a_max, arr[ai])
			a_min = min(a_min, arr[ai])
		# move RHS edge out
		if c_min > max(a_max, b_max) and ci < len(arr) - 1:
			b_min, b_max = min(b_min, arr[ci]), max(b_max, arr[ci])
			ci += 1
			c_max = max(c_max, arr[ci])
			c_min = min(c_min, arr[ci])
		# corner case: totally unsorted
		if ai == 0 and ci == len(arr) - 1:
			return ai, ci

	return ai, ci

