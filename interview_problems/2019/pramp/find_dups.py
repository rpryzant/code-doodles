"""find dups

arr1
arr2

both hold ints 
neither has repeated numbers
 but there are dups across the two
2 cases: same length, one is way longer than the other

find and return dups in sorted order (ascending)


time: 	O(A log A)
space:    A + B

def find_dups(a, b):
	return sorted(list(set(a) & set(b)))


if A ~ B
ordered dict 
scan a, add items
scan b, +1 if in a
scan keys/values, return keys with value > 1

space: A
time: A log A + B + A  


if sorted: scan through both



"""




def find_dups(a, b):
	dups = []
	ai, bi = 0, 0

	while ai < len(a) and bi < len(b):
		if a[ai] == b[bi]:
			dups.append(a[ai])
			ai += 1
			bi += 1
		elif a[ai] < b[bi]:
			ai += 1
		else:
			bi += 1

	return dups



# if one is way bigger, binary search it for each elem in a

def find_dups(a, b):
	dups = []
	bi = 0
	for ai in range(len(a)):
		elem, bi = binary_search(a[ai], b, bi, len(b))
		if a[ai] == elem:
			dups.append(a[ai])
	return dups


def binary_search(x, arr, lo, hi):
	if lo >= hi:
		return arr[hi], hi
	mid = (lo + hi) // 2
	if arr[mid] == x:
		return x, mid
	elif arr[mid] > x:
		return binary_search(x, arr, lo, mid - 1)
	else:
		return binary_search(x, arr, mid + 1, hi)

