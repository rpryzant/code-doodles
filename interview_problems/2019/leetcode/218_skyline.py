[ .. [ li ri hi ] .. ]


1

maintain priority queue with height as sort key
for block in list
add block to pq
look at top of pq
if exausted, pop it and ADD MARK from new head
if new, ADD MARK
otherwise prev best is still cur best so nothing changes


O(n log n) time, O(n) space :( 



2

go back and delete out items from the triples to mark that it’s been exausted

O(n^2) time (might have to go all the way back for each one) 


3

m = SkylineMaxheap()
out = []
for triple in skyline:
    prev_head = m.peek()
m.add(triple)

# first point
if prev_head is None:
    out.append([triple[0], triple[2]])

# new head
elif m.peek() is not prev_head:
    out.append([triple[0], triple[2]])

# same top but exausted
elif prev_head[1] < triple[0]:
    out.append([prev_head[1], m.peek()[2]])
m.pop()

# same top not exausted
else:
    m.pop()

# exaust remaining pq?
