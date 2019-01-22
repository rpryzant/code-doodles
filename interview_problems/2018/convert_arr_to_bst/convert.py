
"""
A = [a1, a2, .., an]

   where a1 <= a2 <= ... <= an

convert to BST:

                  a(n/2)   <-- middle of A

       a(1/4)n                a(3/4)n                     
                  ...      ...        ...

A = [1 2 3 4 5 6 7 8 9 10]
             ^
             r
        ^          ^
     ^    ^     ^     ^
        .... ......


PSEUDOCODE:

validation/base case
    tree is None

make A[n/2] root
root.left = tree from A[1...n/2)
right.right = tree from A(n/2...n]

"""
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

    def printpretty(self):
        self.__printpretty(self, "")

    def __printpretty(self, node, s):
        if node:
            self.__printpretty(node.right, s + "\t")
            print s + str(node.data)
            self.__printpretty(node.left, s + "\t")        


def tree_from_arr(A):
    
    def tfa(l, h):
        if l > h:
            return None
        m = (l + h) / 2

        root = Node(A[m])
        root.left = tfa(l, m - 1)
        root.right = tfa(m + 1, h)

        return root

    return tfa(0, len(A) - 1)



test = [1,2,3,4,5,6,7,8]

out = tree_from_arr(test)

out.printpretty()
