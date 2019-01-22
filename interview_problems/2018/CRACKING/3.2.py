

class Stack:
    def __init__(self):
        self.s = []
        self.mins = []

    def push(self, n):
        self.s.append(n)
        if not self.mins or n < self.mins[-1]:
            self.mins.append(n)

    def pop(self):
        if not self.s:
            return None
        if (len(self.s) == 1) or (self.s[-2] > self.mins[-1]):
            self.mins.pop()
        return self.s.pop()

    def min(self):
        if not self.mins:
            return None
        return self.mins[-1]


s = Stack()
print s.min()
s.push(5)
print s.min()
s.push(4)
s.push(4)
s.push(7)
s.push(3)
s.push(1)
print s.min()
s.pop()
s.pop()
s.pop()
print s.min()
s.pop()
print s.min()
s.pop()
print s.min()
s.pop()
print s.min()
print s.pop()
