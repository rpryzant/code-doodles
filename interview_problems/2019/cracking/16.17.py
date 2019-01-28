"""congiguous sequence



 2  -8  3  -2  4  -10

2  -6 -3  -5  -1  -11
11 -13-5  -8  -6  -10


-5  -5  -5  -5   1   3  -1   4  -5

-5 -10 -15 -20 -19 -16 -17 -13 -18
				  ^ start at righmost peak in forward sum
-18-13  -8  -3   2   1  -2  -1  -5   
		    ^ start at leftmost peak in reverse sum
			(this is going to catch left peak of max)

work inwards:
	while not crossed
		move in peak whose partial sum decreases less


O(N^2): 
1 all sums, take largest
	2 all pairs of peaks from forward and reverse partial sums


O(N):
	peak thing

O(N):
	"""

def get_max_sum(arr):
	max_sum = 0
	tmp = 0
	for x in str:
		tmp += x
		if tmp > max_sum:
			max_sum = tmp
		if tmp < 0:
			tmp = 0

	return max_sum


