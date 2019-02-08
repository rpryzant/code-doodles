paths with sum

given binary tree
COUNT paths that sum to a given value
can paths subsume each other? yes

directinality of paths? > down




for each node
	get all paths
	add count to outgoing sum

O(leaves * log n) time + space

O(log n) by doing this recursively


recurse(node, sofar):
	if node is none:
		return
	increment outgoing ctr if weve completed a sum

	add current node to ongoing sum

	continue ongoing sum down left
	continue ongoing sum down right
	
	start new sum, progress left
	start new sum, progress right























def count_paths(root):
	sum_paths = 0

	def recurse(node, sofar):
		if sofar == target:
			sum_paths += 1

		if node is None:
			return

	sofar += node.data

	recurse(node.left, sofar)
	recurse(node.right, sofar)

	recurse(node.left, node.data)
	recurse(noed.right, node.data)

	recurse(root, 0)
return sum_paths

SP
3

4  0>4
	3  4
	8  4

	3  0
		N 0
		N 3 +1
	8  0
		N 0
		-9 



	4
3		8
	   -9		
	  1
       2
