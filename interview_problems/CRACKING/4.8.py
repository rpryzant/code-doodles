import math

def find_common_ancestor_with_parent_ptr(a, b):
    dif = depth(a) - depth(b)
    forward, lagging = (a, b) if dif < 0 else (b, a)

    for _ in math.abs(dif):
        lagging = lagging.parent

    while id(forward) != id(lagging) and all([forward, lagging]):
        forward = forward.parent
        lagging = lagging.parent

    if not forward or not lagging:
        return None
    return forward




def common_ancestor_no_parent(root, a, b):
    result = common_ancestor(root, a, b)
    if result[1]:
        return result
    return None

def common_ancestor(root, a, b):
    if not root:
        return None
    if root == a or root == b:
        return root, False
    
    left = common_ancestor_no_parent(root.left, a, b)
    right = common_ancestor_no_parent(root.right, a, b)

    if left and right:
        return root, True

    return left or right

