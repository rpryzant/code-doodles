

cache = {}
def biggest_sum(a, i):
	if i in cache: 
		return cache[i]
	if i >= len(a):
		cache[i] = 0
		return cache[i]
	sum = max([
			a[j] + biggest_sum(a, j + 2) 
			for j in range(i, len(a))
		])
	cache[i] = sum
	return cache[i]



print biggest_sum([30, 15, 60, 75, 45, 15, 15, 45], 0)
