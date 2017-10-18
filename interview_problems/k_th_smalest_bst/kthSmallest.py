# i like my solution to this one! O(n) space but it's very readable/cool. plus my
#  way of calculating tree sizes is 100
# in notes

def size(n, d):
    if n.left:
        size(n.left, d)
    if n.right:
        size(n.right, d)
    d[id(n)] = d[id(n.left)] + d[id(n.right)] + 1


def kth_from_last(root, k):
    def _kfl(n, skipped):
        index = d[id(n.left)] + skipped + 1
        if index == k:
            return n
        elif index < k:
            return _kfl(n.right, index)
        else:
            return _kfl(n.left, skipped)
    d = {}
    size(root, d)
    return _kfl(root, 0)



