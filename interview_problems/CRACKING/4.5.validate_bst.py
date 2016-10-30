"""
I really struggled on this one...come back to it!

      7
  4      11
2   6  9   15
"""


class Node(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.data = x


def is_valid(root):

    def check(n, mn, mx):
        if n == None:
            return True

        if (min != None and n.data <= mn) or (max != None and n.data > mx):
            return False

        if not check(n.left, mn, n.data) or not check(n.right, n.data, mx):
            return False

        return True

    return check(root, None, None)



t = Node(7)
t.left = Node(4)
t.left.left = Node(2)
t.left.right = Node(6)

print is_valid(t)
