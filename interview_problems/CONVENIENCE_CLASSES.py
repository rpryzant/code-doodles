
def BiBFS(startA, startB, wList):
    # note this is from word ladder thing
    qA = Queue()
    vA = {startA: 1}
    qA.put(startA)

    qB = Queue()
    vB = {startB: 1}
    qB.put(startB)


    while not qA.empty() or qB.empty():

        xA = qA.get()
        for succ in wList.get_successors(xA):
            if succ in vB:
                return vA[xA] + vB[succ] - 1
            vA[succ] = vA[xA] + 1
            qA.put(succ)

        xB = qB.get()
        for succ in wList.get_successors(xB):
            if succ in vA:
                print xB, succ
                return vB[xB] + vA[succ] - 1
            vB[succ] = vB[xB] + 1
            qB.put(succ)

    return -1

##############################################


def __bfs(self, start, end):
    q = Queue.Queue()
    q.put( (start, [start]) )
    visited = [start]
    while not q.empty():
        pt, cur_path = q.get()
        if self.maze_array[pt[0]][pt[1]] == 'O':
            return cur_path
        neighbors = self.__get_neighbors(pt, visited)
        for neighbor in neighbors:
            cur_path.append(neighbor)
            visited.append(neighbor)
            q.put( (neighbor, cur_path[:]) )
    return None


##############################################################


def swap(a, p, q):
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp

def reverse(a, i, j):
    # reverses i to j in a
    if i == j or i > j: return
    swap(a, i, j)
    reverse(a, i+1, j-1)

#########################################

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
