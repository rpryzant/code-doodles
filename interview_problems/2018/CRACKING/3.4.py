

class MyQueue:
    
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def add(self, x):
        self.s1.append(x)


    def get(self):
        if len(self.s1) == 0:
            return None
        self._transfer(self.s1, self.s2)
        ret = self.s2.pop()
        self._transfer(self.s2, self.s1)
        return ret

    def _transfer(self, a, b):
        for _ in range(len(a)):
            b.append(a.pop())


q = MyQueue()
print q.get()

q.add(5)
print q.get()
q.add(2)
q.add(9)
print q.get()
print q.get()
print q.get()
