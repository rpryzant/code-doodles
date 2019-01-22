"""
given a list of tuples
are we guarenteed that this is a tree? (i.e. that it has a single root?)
   no
self loops? yes

(child parent)

give a bfs traversal of the resulting tree

eg
[('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('c', 'd')]

output: f e a b d c


STEPS

1) build tree (+ get root)
{node: [its children]}

parents = set()
for child, parent in a:
   parents.add(parent)
   if child in parents:
      parents.remove(child)
   d[parent].append(child)

2) traverse tree

out = []
frontier = Queue()
for parent in parents:
   frontier.add(parent)
while not frontier.empty():
   out.append(frontier.pop())
   for child in d[out[-1]]
      frontier.add(child)
return out



hell yeah!! this is better :) 

"""
from collections import deque, defaultdict


def build_order(a, projects):
    if not a:
        return None
    # build graph
    d = defaultdict(list)
    parents = set(projects)
    for child, parent in a:
        if child in parents:
            parents.remove(child)
        d[parent].append(child)

    # traverse graph
    out = []
    frontier = deque([p for p in parents])
    while not len(frontier) == 0:
        x = frontier.pop()  # note: finding dups like this makes it n^2, could be done in n with a final pass as the end
        if x not in out:
            out.append(x)
        frontier.extendleft([child for child in d[out[-1]]])
    return out


projects = ['a', 'b', 'c', 'd', 'e', 'f']
test = [('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('c', 'd')]
print build_order(test, projects)
