


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

# handle assertions, weird cases after

def rotate(n, k):
    # find k-1th to last node (q)
    runner_back = n
    runner_front = n
    for _ in range(k+1):
        runner_front = runner_front.next
    while runner_front is not None:
        runner_back = runner_back.next
        runner_front = runner_front.next

    new_head = runner_back.next
    runner_back.next = None
    new_head.append(n)
    return new_head


n = Node(1)
n.append(2)
n.append(3)
n.append(4)
n.append(5)

print n

print rotate(n, 2)


