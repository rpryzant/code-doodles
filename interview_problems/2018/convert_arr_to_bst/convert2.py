"""
1 2 3 4

     2
  1     3
          4


a = [x1   ..    xn]


base cases:

if a == []
   return None

root = x(n/2)
left = build from a[:n/2]
right = build from a[n/2+1:]
return root

time: logn
space: n logn (all those halves)
  could fix with iterative, or keeping ptrs
"""

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

    def printpretty(self):
        self._printpretty(self, "")

    def __printpretty(self, node, s):
        if node:
            self._printpretty(node.right, s + "\t")
            print s + str(node.data)
            self._printpretty(node.left, s + "\t")        


def convert(a):
    assert all([a[i] <= a[i+1] for i in range(len(a)-1)])

    if a == []:
        return None
    m = len(a) / 2
    root = Node(a[m])
    root.left = convert(a[:m])
    root.right = convert(a[m+1:])
    return root


