"""
in notes
"""


def get_successor(n):
    if n is None:
        return None
    if n.right is not None:
        n = n.right
        while n.left is not None:
            n = n.left
        return n
    else:
        while id(n) != id(n.parent.left) and n.parent is not None:
            n = n.parent
        return n.parent
            
