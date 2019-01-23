

def binary_search(root, x):
    def _bsr(node):
        if node is None:    return None
        if node.data == x:  return node
        elif node.data > x: return _bsr(node.left)
        elif node.data < x: return _bsr(node.rigth)

    return _bsr(root)

