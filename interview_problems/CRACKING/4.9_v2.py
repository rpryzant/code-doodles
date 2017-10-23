

from itertools import product

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sequences(n):
    if n is None:
        return [[]]
    out = []
    left_seqs = sequences(n.left)
    right_seqs = sequences(n.right)
    for l, r in product(left_seqs, right_seqs):
        if l:
            out.append([n.data] + l + r)
        if r:
            out.append([n.data] + r + l)
    if len(out) > 0:
        return out
    return [[n.data]]



root = Node(2)
root.left = Node(1)
root.right = Node(3)

superRoot = Node(4)
superRoot.right = Node(5)
superRoot.left = root

print sequences(root)
print sequences(superRoot)
