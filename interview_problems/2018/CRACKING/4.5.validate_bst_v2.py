"""

a bt is a bst IFF: 
   for each node, left <= root <= right

negative values allowed? 
   sure


       
          7
     4        14
  1        1    18


wahoo!! much better than my first try :)

"""
import sys


class Node(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.v = x




def is_valid(root):

    def recurse(n, low, high):
        if not n:
            return True

        return ( n.v >= low and n.v <= high ) and\
               ( getattr(n.left, 'v', -sys.maxint) <= n.v ) and \
               ( n.v <= getattr(n.right, 'v', sys.maxint) ) and \
               ( recurse(n.left, low, n.v) and recurse(n.right, n.v, high) )

    return recurse(root, root.v, root.v)


t = Node(7)
t.left = Node(4)
t.left.left = Node(2)
t.left.right = Node(6)

print is_valid(t)
