"""
HOLY FUCK!!!!!!



Given a preorder and inorder traversals of a binary tree with unique numbers, reconstruct the original tree, and return a pointer to the root node. Analyze runtime and space complexity

3 5 6 2 4 1      preorder: root, left, right
6 5 3 4 2 1      inorder: left, root, righr

     3
  5
6
"""
class Node:
    def __init__(self, x):
        self.x = x
        self.l = None
        self.r = None


def make_tree(inorder, preorder):
    assert len(inorder) == len(preorder) 
    assert set(inorder) == set(preorder)

    if len(inorder) == 0 and len(preorder) == 0:
        return None

    if inorder == preorder:
        return Node(inorder[0])

    root = preorder[0]
    leftmost = inorder[0]
    
    left_inorder = inorder[: inorder.index(root)]
    left_preorder = preorder[1 : preorder.index(leftmost) + 1]

    right_inorder = inorder[inorder.index(root) + 1:]
    right_preorder = preorder[preorder.index(leftmost) + 1:]

    out = Node(root)
    out.l = make_tree(left_inorder, left_preorder)
    out.r = make_tree(right_inorder, right_preorder)

    return out


pre = [3, 5, 6, 2, 4, 1]
ino = [6, 5, 3, 4, 2, 1]

n = make_tree(ino, pre)
print n.x
print n.l.x
print n.r.x
