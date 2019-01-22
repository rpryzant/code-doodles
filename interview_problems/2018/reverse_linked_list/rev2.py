


class Node:

    def __init__(self, x):
        self.next = None
        self.x = x

    def append(self, x):
        if self.next == None:
            self.next = Node(x)
        else:
            self.next.append(x)

    def __str__(self):
        return '%s ==> %s' % (self.x, str(self.next))


def reverse(n):
    prev = None
    cur = n
    next = getattr(n, 'next', None)
    while cur != None:
        cur.next = prev
        prev = cur
        cur = next
        next = getattr(next, 'next', None)
    return prev

n = Node(1)
n.append(2)
n.append(3)
n.append(4)

print n
print reverse(n)

