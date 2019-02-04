"""K-messed array sort

if a is a sorted array:


def permute(x):
	return x[0] + int((k + 1) * random.random())

a_in = sorted(enumerate(a), key=permute)



corner cases to look out for
	empty array
	already sorted
	0 k
k > len(array)

ideas for general case

1: brute force: sort array O(n log n)

2: 
[  ...  a_i-k a_i-k+1 ..  a_i    … ]

min heap! 

zip through array, loading things into min heap
once heap is size k, pop the min from it as you move forward in the array

O(n log k)

pseudocode

	empty array -- fine
	already sorted -- fine
	0 k --fine (will just start popping right away)
k > len(array)  bad! need to count for this


arr = [1 4 5 2"""




def kmessed(arr):
	if k > len(arr):
			return arr

	for i, x in enumerate(arr):
			heap.push(x)
		if i >= k:
				arr[i - k] = heap.pop()

	for i in range(k)[::-1]:
			arr[-i] = heap.pop()

	return arr
