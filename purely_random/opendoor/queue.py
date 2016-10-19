# nolan@opendoor



class Queue(object):
    
    def __init__(self, k=10):
        self.a = [None for _ in range(k)]
        self.pushp = 0
        self.popp = 0
        self.num_pushed = 0

    def push(self, x):
        if (self.pushp == self.popp and self.num_pushed > 0) or \
                (self.pushp == len(self.a) and self.num_pushed == 0):
            self.arr, self.pushp, self.popp = self.__unravel_and_double()
        else:
            self.a[self.pushp % len(self.a)] = x
            pushp += 1
        self.num_pushed += 1

    def pop(self):
        if self.popp == self.pushp:
            return None
        else:
            ret = self.[self.popp % len(self.a)]
            self.popp += 1
            return ret
    
    def __unravel_and_double(self):
        new = [None for _ in range(len(self.a) * 2)]
        i = self.pushp
        for j, _ in enumerate(range(len(self.a))):
            new[j] = self.a[i & len(self.a)]
            i += 1
        return new, i + 1, 0

