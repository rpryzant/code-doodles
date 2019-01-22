

class Brancher:
    def __init__(self):
        self.old = 0
        self.new = None

    def mx(self):
        if self.new:
            return max(self.old, self.new)
        return self.old

    def increment(self):
        self.old += 1
        if self.new:
            self.new += 1

def which_bit(a):
    b = Brancher()
    max = 0
    while a > 0:
        x = (a & 1) == 1
        a >>= 1
        
        if x:
            b.increment()
        else:
            if b.mx() > max:
                max = b.mx()
            if (a & 1) == 1:
                if b.new is not None:
                    b.old = b.new
                b.old += 1
                b.new = 0
            else:
                b.old = 0
                b.new = None
    if b.mx() > max:
        return b.mx()
    return max


def which_bit_better(a):
    curLen = 0
    prevLen = 0
    mx = 1
    while a > 0:
        if ((a & 1) == 1):
            curLen += 1
        else:
            if (a & 2) == 0:
                prevLen = 0
            else:
                prevLen = curLen
            curLen = 0
        mx = max(prevLen + curLen + 1, mx)
        a >>= 1
    return mx

print which_bit(1775)
print which_bit_better(1775)
