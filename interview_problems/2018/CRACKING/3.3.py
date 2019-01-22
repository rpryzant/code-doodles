
class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.C = capacity

    def push(self, x):
        if not self.stacks:
            self.stacks.append([])
        if len(self.stacks[-1]) == self.C:
            self.stacks.append([])
        sefl.stacks[-1].append(x)

    def pop(self):
        if not self.stacks:
            return None
        x = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return x

    def pop_at(self, i):
        if i < 0 or i > len(self.stacks):
            return None
        x = self.stacks[i].pop()
        if not self.stacks[i]:
            del self.stacks[i]
        return x



