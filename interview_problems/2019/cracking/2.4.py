"""
partition
take a linked list and an x

return a linked list such that 
all y : y < x is left of x
all y : y >= x is right of x

O(n) pseudocode

for each node
if node.data < x
set or add node to less_than list
else
set or add node to greater_than list

point tail of less_than to head of greater_than
( O(n) or O(1) depending on implementation )
watch out! one of these could be none
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def partition(root, x):
    left_head, left_tail = None, None
    right_head, right_tail = None, None
    
    while root is not None:
        if root.data < x:
            if less_head:
                less_tail.next = root
                less_tail = less_tail.next
            else:
                less_head = root
                less_tail = root
        else:
            if right_head:
                right_tail.next = root
                right_tail = right_tail.next
            else:
                right_head = root
                right_tail = root

    if left_tail:
        left_tail.next = right_head
        return left_head
    else:
        return right_head


