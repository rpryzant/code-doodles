## this is better!! accounts for a hidden corner case






class Node(object):
    def __init__(self, d):
        self.d = d
        self.next = None

    def append(self, x):
        if self.next is None:
            self.next = Node(x)
        else:
            self.next.append(x)

    def __str__(self):
        return '%s => %s' % (str(self.d), str(self.next))


def sum(a, b):
    out = None
    carry = 0
    while a is not None or b is not None or carry > 0:
        tmp = getattr(a, 'd', 0) + getattr(b, 'd', 0) + carry
        carry = tmp / 10
        tmp %= 10
        if out is None:
            out = Node(tmp)
        else:
            out.append(tmp)
        a = a.next
        b = b.next
    return out


def sum_reverse(n1, n2):
    def recurse(a, b):
        if a is None and b is None:
            return (None, 0)

        sofar, carry = recurse(getattr(a, 'next', None), getattr(b, 'next', None))

        tmp = getattr(a, 'd', 0) + getattr(b, 'd', 0) + carry
        carry = tmp / 10
        tmp %= 10

        out = Node(tmp)
        out.next = sofar

        return out, carry

    sofar, carry = recurse(n1, n2)
    if carry > 0:
        tmp = Node(carry)
        tmp.next = sofar
        sofar = tmp
    return sofar


t1 = Node(7)
t1.append(1)
t1.append(6)

t2 = Node(5)
t2.append(9)
t2.append(2)

print sum(t1, t2) 


t1 = Node(6)
t1.append(1)
t1.append(7)

t2 = Node(2)
t2.append(9)
t2.append(5)

print sum_reverse(t1, t2)
