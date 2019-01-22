from collections import defaultdict

class Node:
    def __init__(self, val):
        self.next = None
        self.data = val
        self.length = 1

    def append(self, num):
        self.length += 1
        new = Node(num)
        while self.next:
            self = self.next
        self.next = new

    def __str__(self):
        s = ''
        while self:
            s += "%s => " % self.data
            self = self.next
        return s


def find_loop(head):
    d = defaultdict(lambda: False)
    runner = head
    while runner.next is not None:
        if d[id(runner)]:
            return runner
        d[id(runner)] = True
