"""

      node
 less         more
(also bst)  (also bst)


if node is none
   return true

make sure left and right child are valid

make sure left < parent < right


if n is None:
   return True

if not valid(n.left) or not valid(n.right):
   return False

if n.left.data >= n.data or n.right.data <= n.data:
   return False

return True

"""
def valid(n):
    if n is None:
        return None

    if not valid(n.left) or not valid(n.right):
        return False

    if n.left.data >= n.data or n.right.data <= n.data:
        return False

    return True



