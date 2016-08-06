# TODO
#     FIX DOUBLE ADD PROBLEM!!
#          ====> circular ll

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
    def pp(self):
        s = ''
        tmp = self
        while tmp != None:
            s += "%s %s | "% (tmp.key, tmp.value)
            tmp = tmp.next
        print s


class LRU:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.d = {}
        self.head = None
        self.tail = None

    def add(self, key, value):
        if len(self.d) == self.maxsize:
            self.__removeTail()
        new = Node(key, value)
        self.d[key] = new
        self.__moveToHead(new)

    def __removeTail(self):
        del self.d[self.tail.key]
        self.tail = self.tail.next
        self.tail.prev = self.head

    def __moveToHead(self, n):
        if self.head is n:
            return
        elif self.head is None:
            self.head = n
            self.tail = n
            n.next = n
            n.prev = n
        else:
            if n is self.tail:
                self.tail = n.next
            if n.next:
                n.next.prev = n.prev
            if n.prev:
                n.prev.next = n.next
            n.next = None
            n.prev = self.head
            self.head.next = n
            self.head = n

    def remove(self, key):
        if not self.d.get(key):
            return
        n = d[key]
        n.next.prev = n.prev
        n.prev.next = n.next
        n = None

    def contains(self, key):
        if not self.d.get(key):
            return False
        self.__moveToHead(self.d[key])
        return True

    def __str__(self):
        s = ''
        runner = self.head
        while True:
            s += '[%s : %s] => ' % (runner.key, runner.value)
            runner = runner.prev
            if runner is self.tail:
                return s

l = LRU(4)

l.add(1,0)
print l
l.contains(1)
#l.add(1,0)
print l

l.add(2,0)
print l
l.contains(2)
print l
l.contains(1)
print l
l.add(3,0)
l.add(4,0)
print l
l.add(5,0)
print l
l.contains(2)
print l
l.contains(3)
print l
