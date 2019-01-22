"""
in notes

"""
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


def is_palindrome(head):
    if not head:
        return False
    l = head.length
    s = []
    t = head
    for _ in range(l/2):
        s.append(t.data)
        t = t.next
    if l % 2:
        t = t.next
    while t is not None:
        x = s.pop()
        if t.data != x:
            return False
        t = t.next
    if len(s) > 0:
        return False
    return True

n = Node('0')
n.append('1')
n.append('1')
n.append('5')
n.append('1')
n.append('1')
n.append('0')
print n
print is_palindrome(n)
    
n = Node('0')
n.append('1')
n.append('5')
n.append('1')
n.append('1')
n.append('0')
print n
print is_palindrome(n)

n = Node('0')
n.append('1')
n.append('1')
n.append('0')
print n
print is_palindrome(n)

n = Node('0')
print n
print is_palindrome(n)

