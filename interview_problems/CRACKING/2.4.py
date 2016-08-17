

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def append(self, new):
        while self.next is not None:
            self = self.next
        self.next = new

    def __str__(self):
        s = ''
        while self is not None:
            s += '%s => ' % self.data
            self = self.next
        return s

def moveNode(n, r):
    t = r.next
    r.next = r.next.next
    t.next = n.next
    n.next = t

def partition(head, x):
    n = head
    # move lhead to front (first node with value < x)
    if n.data < x:
        lhead = n
    else:
        while n.next is not None and n.next.data  >= x:
            n = n.next
        if n.next is not None:
            t = n.next
            n.next = n.next.next
            t.next = head
            lhead = t
    # move ghead to 2nd place (first node with value > x)
    t = lhead
    while t.next is not None and t.next.data < x:
        t = t.next
    if t.next is None:  # done - all elements are < x
        return lhead
    moveNode(lhead, t)
    ghead = lhead.next
    # zip through list, adding after lhead if < x, let be if > x (because runner is at tail of ghead list)
    r = ghead
    while r.next is not None:
        if r.next.data < x:
            moveNode(lhead, r)
        else:
            r = r.next
    return lhead


n = Node(3)
n.append(Node(5))
n.append(Node(8))
n.append(Node(5))
n.append(Node(10))
n.append(Node(2))
n.append(Node(1))
print n
print partition(n, 5)
