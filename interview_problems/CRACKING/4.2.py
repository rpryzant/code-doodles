
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

    def __str__(self):
        s = ''
        s += '%s\t' % str(self.right)
        s += '%s\n' % self.data
        s += '%s\t' % str(self.left)
        return s


def bst(a):
    return __bst(a, 0, len(a) - 1)

def __bst(a, l, h):
    if l > h:
        return None
    m = (l+h)/2
    root = Node(a[m])
    root.left = __bst(a,l,m-1)
    root.right = __bst(a, m+1, h)
    return root


print str(bst([1,2,3,4,5,6,7]))
print str(bst([1,2,3,4,5,7]))
