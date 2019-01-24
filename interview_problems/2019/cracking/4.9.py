""" this one works! last had a bug"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sequences(root):
    out = []
    def _aar(node, cur, waiting):
        if node:
            cur.append(node.data)
            if node.left: waiting += [node.left]
            if node.right: waiting += [node.right]

        if not waiting:
            out.append(cur)
            return

        for i, next_node in enumerate(waiting):
            _aar(next_node, cur[:], waiting[:i] + waiting[i+1:])
    
    _aar(root, [], [])

    return out




root = Node(2)
root.left = Node(1)
root.right = Node(3)

superRoot = Node(4)
superRoot.right = Node(5)
superRoot.left = root

print sequences(root)
print sequences(superRoot)
