"""find dups


N = max num (unknown)
A = array size (known...big)
M = memory (4kb ~ 4k numbers if short)


O(A * (N/M)): 
	for each pass of array look for numbers in [i*m, (i+1)*m]


what can i use the mem for? holding
	indices
	numbers from A
		^^ similar, but not identical as dups have same number but dif index
	
	counts
		most space efficient
		doesn’t require second dup-finding pass


problem! don’t know N -- how many passes?
	find max O(1)
"""

def print_dups(arr):
	N = min(max(arr), 32000)
	for i in range(N / 4000):
		buffer = [0] * 4000
		for x in arr:
			if x > i * 4000 and x < (i+1) * 4000:
				if buffer[x - (i * 4000)] == 1:
					print(x)
				else:
					buffer[x - (i * 4000)] += 1

