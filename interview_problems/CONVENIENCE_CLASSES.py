
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


    
# line (y = mx + b)  
class Line:
      def __init__(self, m, b):
            self.m = m
            self.b = b
            
      @staticmethod
      def gen_line(a, b):
            if a.x == b.x:
                  return None

            m = float(b.y - a.y) / (b.x - a.x)
            b = b.y - b.x * m
            return Line(m, b)

      def f(self, x):
            return self.m * x + self.b

      def search(self, pts):
            return sum(1 if self.f(p.x) == p.y else 0 for p in pts)

      def __str__(self):
            return "y = %sx + %s" % (self.m, self.b)

    

def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return reduce(gcd, numbers)

# Least common multiple is not in standard libraries? It's in gmpy, but this is simple enough:

def lcm(*numbers):
    """Return lowest common multiple."""    
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

# Assuming numbers are positive integers...
