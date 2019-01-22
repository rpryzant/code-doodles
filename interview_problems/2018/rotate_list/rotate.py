


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.length = 1

    def append(self, num):
        if not self.next:
            self.next = Node(num)
        else:
            self.next.append(num)
        self.length += 1


    def __str__(self):
        return "%s => %s" % (self.data, str(self.next))





def rotate(head, k):
    l = head.length
    k = k % l
    r = head
    for _ in range(l - k - 1):
        r = r.next
    tmp = r.next
    r.next = None
    r = tmp
    while r.next:
        r = r.next
    r.next = head
    head = tmp
    return head


test2 = Node(1)
test2.append(2)
test2.append(3)
test2.append(4)
test2.append(5)

print test2
print rotate(test2, 2)


test2 = Node(1)
test2.append(2)
test2.append(3)
test2.append(4)
test2.append(5)

print rotate(test2, 7)
