

class binode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def printpretty(self):
        self.__printpretty(self.root, "")

    def __printpretty(self, node, s):
        if node:
            self.__printpretty(node.right, s + "\t")
            print s + str(node.data)
            self.__printpretty(node.left, s + "\t")

    def ___str__(self):
        print 'here'
        s = str(self.data)
        if not self.left and not self.right:
            return s
        if self.left:
            s = str(self.left) + " => " + s
        if self.right:
            s = s + " => " + str(self.right)
        return s


def make_list(root):
    if not root:
        return None, None
    if not root.left and not root.right:
        root.left = root.right = None
        return root, root

    lh = lt = rh = rt = None
    if root.left:
        lh, lt = make_list(root.left)
    if root.right:
        rh, rt = make_list(root.right)

    root.left = lt
    if lt:
        lt.right = root

    root.right = rh
    if rh:
        rh.left = root
    return (lh or root), (rt or root)


test = binode(5, None, binode(7))


print make_list(test)[0]
