


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
    carry = 0
    out = Node(-1)
    while a is not None or b is not None or carry > 0:
        da = getattr(a, 'd', 0)
        db = getattr(b, 'd', 0)
        out.append((da + db + carry) % 10)
        carry = (da + db + carry) / 10
        a = a.next
        b = b.next
    return out.next


t1 = Node(7)
t1.append(1)
t1.append(6)

t2 = Node(5)
t2.append(9)
t2.append(2)

print sum(t1, t2)



# can
#   1 reverse, then call sum
#   2 read into reversed buffer like stack and then add
#   recursively add rest of lists, then do last addition (percolate answers backwards)
def sum_reverse(a, b):
    def sr(l1, l2):
        if l1 is None and l2 is None:
            return None, 0

        sofar, carry = sr(getattr(l1, 'next', None), getattr(l2, 'next', None))
        tmp = getattr(l1, 'd', 0) + getattr(l2, 'd', 0) + carry

        new = Node(tmp % 10)
        new.append(sofar)

        return new, tmp / 10

    return sr(a, b)[0]


t1 = Node(6)
t1.append(1)
t1.append(7)

t2 = Node(2)
t2.append(9)
t2.append(5)



print sum_reverse(t1, t2)
