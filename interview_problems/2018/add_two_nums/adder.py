# in notes

class Node:
    def __init__(self, d):
        self.next = None
        self.data = d
        
    def append(self, x):
        n = Node(x)
        r = self
        while r.next is not None:
            r = r.next
        r.next = n

    def __str__(self):
        s = ''
        r = self
        while r is not None:
            s += '%s => ' % r.data
            r = r.next
        return s

def add_lists(a, b):
    out = None
    carry = 0
    while any([a,b,carry]):
        s = getattr(a, 'data', 0) + getattr(b, 'data', 0) + carry
        if out is None:
            out = Node(s % 10)
        else:
            out.append(s % 10)
        carry = s / 10
        a = getattr(a, 'next', None)
        b = getattr(b, 'next', None)
    return out


a = Node(2)
a.append(4)
a.append(3)

b = Node(5)
b.append(6)
b.append(4)

print add_lists(a, b)
