"""smallest difference

two arrays
	a
	b

contents are 
	1 integers
	positive
	non-empty
	balanced? 
	not sorted

want to find smallest difference
	is this a-b or b-a? or abs()?



O(n^2)
for ai in a
	for bi in b
		if ai-bi is new min, set min

O(n log n)
sort both arrays
step through both, moving pointer for whichever array would make smaller diff
guarentees that you’ll find global min because

	the global min is going to occur between nearby nums
	for every number, we visit its nearest neighbors 
		(both are sorted, we are starting at the smallest, only increasing
			the nearer side)

faster?
	log n? 
		do some kidn of fancy binary earch based on diffs
			⇒ no, no ordering to arrays
[113, 3, 4, 11, 43]
[64, 19, 46, 2, 0]
[3, 2]



smallest dif
	ai bi is 0
	while not done
		if dif(ai, bi) < smallest:
			update smallest
		if dif(ai+1, bi) < dif(ai, bi+1):
			ai += 1
		else
			bi+= 1
"""

def smallest_dif(a, b):
	def dif(ai, bi): return abs(a[ai] - b[bi])
	a = sorted(a)
	b = sorted(b)
	ai, bi = 0, 0

	min_pair = None
	while ai < len(a) and bi < len(b):
		if not min_pair or dif(ai, bi) < min_val:
			min_pair = ai, bi
		# move non-exausted forward
		if ai == len(a) - 1 :
			bi += 1
		elif bi == len(b) - 1:
			ai += 1
		# move smaller forward
		if dif(ai + 1, bi) < dif(ai, bi + 1):
			ai += 1
		else:
			bi += 1



def smallest_dif_v2(a, b)
	a = sorted(a)
	b = sorted(b)
	ai, bi = 0, 0
	min = None
	while ai < len(a) and bi < len(b):
		if not min or abs(a[ai] - b[bi]) < abs(min[0] - min[1]):
			min = ai, bi
		if ai < len(a) - 1 and a[ai] < b[bi]:
			ai += 1
		elif bi < len(b) - 1:
			bi += 1
		
		
		
		
		
	




