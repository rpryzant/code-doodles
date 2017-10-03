

class MinStack:
    def __init__(self):
        self.data = []
        self.mins = []

    def push(self, x):
        self.data.append(x)
        if not self.mins or x < self.mins[-1]:
            self.mins.append(x)

    def pop(self):
        out = None if not self.data else self.data.pop()
        if out and out == self.mins[-1]:
            self.mins.pop()
        return out

    def min(self):
        return None if not self.mins else self.mins[-1]



s = MinStack()
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



