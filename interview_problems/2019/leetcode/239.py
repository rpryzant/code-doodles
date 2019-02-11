"""
DIDN"T GET SOMETHING FAST

O(nk)

sliding window max

def sliding_window_max(a, k):
	out = []
	for i in range(len(a) - k):
		out += max(a[i: i + k])
	return out

O(n)


min heap instead of max each time
	O(n log k)

[x_1  [x_i   ..   x_i+k] x_i+k+1     x_n]
[x_1  x_i [x_i+1   ..   x_i+k x_i+k+1]     x_n]

cases:
	max of window i is x_i
	x_i+k+1 is max of window i+1      
	x_i+k+1 is not max of window i+1
	max of window i is not x_i
	x_i+k+1 is max of window i+1     
	x_i+k+1 is not max of window i+1

queue of maxs
	put fresh maxs on top of queue (or fill empty queue)
	if element leaving window is equal to back of queue, pop from back


[10, 9, 1, 1, 1]
[10, 9, 1, 1, 1]
# a less than k? 
queue = [max(a[0: k])]
out = [queue[-1]]
for x in a[k + 1:]:
	if not queue or x > queue[-1]:
		queue.append(x)
	elif x == queue[0]:
		queue = queue[1:]
	out.append(queue[-1])

return out

two passes from both sides?
windowing max? 
"""

