





class TripleStack(object):

    class SubStack(object):
        def __init__(self, arr, start, end):
            self.arr = arr
            self.start = start
            self.end = end
            self.cur = start

        def empty(self):
            return self.cur == self.start
        
        def full(self):
            return self.cur > self.end

        def push(self, x):
            if self.full():
                return
            self.arr[self.cur] = x
            self.cur += 1

        def pop(self):
            if self.empty():
                return None
            self.cur -= 1
            ret = self.arr[self.cur]
            return ret

        def iter(self):
            for i in range(self.start, self.cur):
                yield self.arr[i]


    def __init__(self, initial_size=10):
        self.arr = [None for _ in range(initial_size / 2)]
        self.stacks = None
        self.__double()

    def __double(self):
        new = [None for _ in range(len(self.arr) * 2)]
        ss_size = len(new) / 3
        new_stacks = [
            self.SubStack(new, 0, ss_size),
            self.SubStack(new, ss_size + 1, 2 * ss_size),
            self.SubStack(new, (2 * ss_size) + 1, len(self.arr) - 1)
            ]

        if self.stacks is not None:
            for i, stack in enumerate(self.stacks):
                for x in stack.iter():
                    new_stacks[i].push(x)
        self.arr = new
        self.stacks = new_stacks


    def push(self, ss_i, x):
        if self.stacks[ss_i].full():
            self.__double()
        self.stacks[ss_i].push(x)

    def pop(self, ss_i):
        return self.stacks[ss_i].pop()




ts = TripleStack()

ts.push(1, 0)
ts.push(1, 2)
ts.push(1, 3)
print ts.arr
ts.push(1, 4)
print ts.arr
ts.push(1, 5)
ts.push(1, 6)
print ts.arr
ts.pop(1)
ts.pop(1)
ts.pop(1)
ts.pop(1)
ts.pop(1)
print ts.pop(1)
print ts.pop(1)
print ts.pop(1)

ts.push(0, 0)
ts.push(1, 1)
ts.push(2, 0)
print ts.arr
print ts.pop(1)
