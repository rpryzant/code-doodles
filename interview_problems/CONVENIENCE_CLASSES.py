
# binary tree
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

    def printpretty(self):
        self._printpretty(self, "")

    def _printpretty(self, node, s):
        if node:
            self._printpretty(node.right, s + "\t")
            print s + str(node.data)
            self._printpretty(node.left, s + "\t")        

# linked list
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def append(self, new):
        while self.next is not None:
            self = self.next
        self.next = new

    def get_tail(self):
        if not self.next:
            return self
        else:
            return self.next.get_tail()
        
    def __str__(self):
        s = ''
        while self is not None:
            s += '%s => ' % self.data
            self = self.next
        return s


