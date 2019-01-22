# i like my solution to this one!



class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def printpretty(self):
        self.__printpretty(self, "")

    def __printpretty(self, node, s):
        if node:
            self.__printpretty(node.right, s + "\t")
            print s + str(node.data)
            self.__printpretty(node.left, s + "\t")





def gen_trees(n):
    def gtr(s, e):
        if s > e:
            yield None
        for pivot in range(s, e+1):
            for lsubtree in gtr(s, pivot - 1):
                for rsubtree in gtr(pivot + 1, e):
                    root = Node(pivot)
                    root.left = lsubtree
                    root.right = rsubtree
                    yield root
    return [tree for tree in gtr(1, n)]

print len(gen_trees(3))
for tree in gen_trees(3):
    tree.printpretty()
    print '==========='
