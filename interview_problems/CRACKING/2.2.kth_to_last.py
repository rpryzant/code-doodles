"""


n1 -> n2 -> ... n(l - (k - 1)) -> ... -> nl


e.g. k = 3
1 2 3 4 5 6 7 8 9
            6
1   2

1) send runner k-1 steps into the list
2) iterate lagging, runner 1 step at a time
3) when runner.next == None, return lagging
"""


class Node(object):
    def __init__(self, d):
        self.d = d
        self.next = None

    def append(self, x):
        if self.next is None:
            self.next = Node(x)
        else:
            self.next.append(x)


# pre: len(head) >= k
def kth_to_last(head, k):
    r = head
    for _ in range(k-1):
        r = r.next
    f = head
    while r.next is not None:
        f = f.next
        r = r.next
    return f



test = Node(1)
test.append(2)
test.append(3)
test.append(4)
test.append(5)
test.append(6)
test.append(7)

print kth_to_last(test, 1).d
