"""BUILD ORDER



projects
    list of string ids
    no order
    no dups
    size?

dependancies
list of pairs of ids
guaranteed to occur in projects 
order doesnt matter

what about projects that dont occur in dependancies?
    no dependancy so can do whenever

any guarentees on graph topology? e.g. how many roots? no

a, b, c, d, e, f
(a, d), (f, b), (b, d), (f, a), (d, c)

  f
a   b
  d
  c

e

dict of id: node, go through and set pointers and then traverse the graph you just made
    O(N) space
    O(N + N) time (make nodes + traverse)






a, b, c, d, e, f
(a, d), (f, b), (b, d), (f, a), (d, c)

f
a   b
  d
  c
e
"""

class Node:
    def__init__(self, id):
        self.id = id
        self.parents = []
        self.children = []
        self.is_root = True

    def set_child(self, n):
        self.children.append(n.id)

    def set_parent(self, n):
        self.parents.append(n)
        self.is_root = False

    def disown(self, parent_id):
        del self.parents[self.parents.index(parent_id)]
        if len(self.parents) == 0:
            self.is_root = True

def build_tree(ids, deps):
    table = {id: Node(id) for id in ids}
    for parent, child in deps:
        table[parent].set_child(child)
        table[child].set_parent(parent)

def breadth_traverse(table):
    queue = [
        id for id, node in table.items() if node.is_root
    ]
    out = []
    while len(queue) > 0:
        cur = queue.pop()
        out.append(cur)
        for child in cur.children:
            child.disown(cur)
            if child.is_root and child not in queue:
                queue.append(child)
    return out


def build_order(ids, deps):
    tree_table = build_tree(ids, deps)
    ids = breadth_traverse(tree_table)
    return ids

p = ['a','b','c','d','e','f']
d = [('d','a'),('b','f'),('d','b'),('a','f'),('c','d')]
print build_order(p,d)
