"""

             8
       9          10             max depth = 8-10-1-2-4=**5**
    2     3     1
 2                2
                    4

"""



class Node:
    def __init__(self, d):
        self.left = None
        self.right = None
        self.data = d


def max_depth(n):
    def md(n, cur):
        if not n:
            return cur
        else:
            return max(md(n.left, cur + 1), md(n.right, cur + 1))
    return md(n, 0)




n = Node(8)
n.left = Node(9)
n.right = Node(10)
n.right.left = Node(1)
n.right.left.right = Node(2)

print max_depth(n)
