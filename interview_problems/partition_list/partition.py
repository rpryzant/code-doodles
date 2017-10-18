# in notes

class Node:
    def __init__(self, d):
        self.d = d
        self.next = None
        
    def append(self, new):
        if not self.next:
            self.next = new
        else:
            self.next.append(new)

    def get_tail(self):
        if not self.next:
            return self
        else:
            return self.next.get_tail()

    def __str__(self):
        out = '%s =>' % self.d
        out += str(self.next)
        return out


def partition(head, x):
    lh = gh = None
    r = head
    while r is not None:
        tmp = r.next
        if r.d < x:
            if not lh:
                lh = r
            else:
                lh.append(r)
        else:
            if not gh:
                gh = r
            else:
                gh.append(r)
        r.next = None
        r = tmp

    lh.get_tail().next = gh

    return lh








test = Node(1)
test.append(Node(4))
test.append(Node(3))
test.append(Node(2))
test.append(Node(5))
test.append(Node(2))

print test
print partition(test, 3)
        
