


class Node:
    def __init__(self, d):
        self.left = None
        self.right = None
        self.d = d





def path_sum(n, t):

    def path_sum(n, sofar):
        sofar.append(n.d)

        if n.left is None and n.right is None:
            if sum(sofar) == t:
                return [sofar]
            else:
                return []

        left = [] if not n.left else path_sum(n.left, sofar[:])
        right = [] if not n.right else path_sum(n.right, sofar[:]) 

        return left + right

    return path_sum(n, [])







n = Node(5)
n.left = Node(4)
n.right = Node(8)
n.left.left = Node(11)
n.left.left.left = Node(7)
n.left.left.right = Node(2)
n.right.left = Node(13)
n.right.right = Node(4)
n.right.right.left = Node(5)
n.right.right.right = Node(1)


print path_sum(n, 22)
    
