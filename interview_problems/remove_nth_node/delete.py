

class Node:
    def __init__(self, d):
        self.next = None
        self.data = d

    def append(self, n):
        while self.next is not None:
            self = self.next
        self.next = n


    def __str__(self):
        s = ''
        while self is not None:
            s += '%s => '% self.data
            self = self.next
        return s

def remove_from_list(n, p):
    if p < 1:
        print 'error'
        return 0
    r = n
    while p > 1:
        r = r.next
        p -= 1
        if r is None:
            print "error"
            return 0

    while r is not None and getattr(r.next, 'next', None) is not None:
        n = n.next
        r = r.next

    n.next = getattr(n.next, 'next', None)
    return 1


root = Node(1)
root.append(Node(2))
root.append(Node(3))
root.append(Node(4))
root.append(Node(5))
print(root)

remove_from_list(root, 2)
print root

remove_from_list(root, 8)
print root

remove_from_list(root, 1)
print root

remove_from_list(root, 0)
print root

remove_from_list(root, 1)
remove_from_list(root, 1)
print root


remove_from_list(root, 1)
print root
