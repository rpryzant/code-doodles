# in notes

from collections import defaultdict

class Point:
      def __init__(self, x, y):
            self.x = x
            self.y = y

      def equals(self, other):
            return self.x == other.x and self.y == other.y


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

# O(n^3) because search() is O(n)
def find_max_line(pts):
      lines = []
      max = 0
      maxl = None
      for a in pts:
            for b in pts:
                  if a.equals(b):
                        continue
                  l = Line.gen_line(a, b)
                  if l is not None and l not in lines:
                        lines.append(l)
                        num_p = l.search(pts)
                        if num_p > max:
                              max = num_p
                              maxl = l

# O(n^2)
def find_max_line_better(pts):
      max = 0
      maxl = None
      d = defaultdict(lambda: 0)
      for a in pts:
            for b in pts:
                  if a.equals(b):
                        continue
                  l = Line.gen_line(a, b)
                  if l:
                        d[(l.m, l.b)] += 1
                        max, maxl = (max, maxl) if max > d[(l.m, l.b)] else (d[(l.m, l.b)], l)
      return maxl

test = [Point(0,0), Point(1,1), Point(1,2), Point(2,2)]
print find_max_line(test)
test = [Point(0,0), Point(1,1), Point(1,2), Point(2,2)]
print find_max_line_better(test)
