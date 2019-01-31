"""living people

list of people, birth and death years
find year when most people alive

does birth year count as alive? yes
does death year count as alive? yes
input = [
	[birth_0, death_0]
	[birth_1, death_1]
]

birth_i > 1900 for all i
deaths exist

find year with most people alive

[1 5]
[2 2]
[3 6]
[4 4]
4

sorted? no

1
	sort, ininsert deaths with binary search, read off max
		O(n log n + n log n + n)
2
	pass 1: mark array with births
	pass 2: mark array with deaths
	pass 3: read off max

	O(100 + 100) space, O(n + n + n) time
3
	pass 1: mark array with births (+1) and deaths (-1)
	pass 2: read off max

	close to optimal, because at the very least you need some way of keeping track of how many people were alive before each death
"""








def pop(people):
	pop_deltas = [0] * 200
	for (birth, death) in people:
		pop_deltas[birth % 1900] += 1
		if death != birth:
			pop_deltas[death % 1900] -= 1

	tmp, max, maxi = 0, -1, -1
	for i, x in enumerate(pop_deltas):
		tmp += x
		if tmp > max:
			max = tmp
			maxi = i
	return maxi + 1900

print pop([
	[1900, 1999],
	[1910, 1980],
	[1950, 1953],
	[1952, 1952]
])