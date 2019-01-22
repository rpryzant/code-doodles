
class Node:
    def __init__(self, d):
        self.d = d
        self.next = None
        self.len = 1

    def append(self, n):
        self.len += 1
        if not self.next:
            self.next = n
        else:
            self.next.append(n)

    def __str__(self):
        return str(self.d) + ' => ' + str(self.next)




def reverse_part(head, m, n):
    if head is None or m < 0 or n > head.len:
        return head

    # kind of a hack for this corner case...but it works
    if m == 1:
        start = Node(0)
        start.next = head
    else:
        start = head
        for _ in range(m - 2):
            start = start.next

    end = start
    for _ in range(n - m + 2):
        end = getattr(end, 'next', None)

    h, t = rev_chunk(start.next, n - m + 1)
    
    start.next = h
    t.next = end

    if m == 1:
        return h
    else:
        return head


def rev_chunk(n, l):
    prev = None
    cur = n
    next = n.next
    for _ in range(l):
        cur.next = prev
        prev = cur
        cur = next
        next = getattr(next, 'next', None)
    return prev, n




test = Node(1)
test.append(Node(2))
test.append(Node(3))
test.append(Node(4))
test.append(Node(5))
print test


#print reverse_part(test, 2, 4)

#print reverse_part(test, 2, 5)

#print reverse_part(test, 1, 5)

print reverse_part(test, 1, 3)

