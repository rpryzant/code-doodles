# had to look up a working solution...not every problem is a win


from collections import defaultdict


class Node:
    def __init__(self, s):
        self.s = s
        self.left = None
        self.right = None

    def printpretty(self):
        self.__printpretty(self, "")

    def __printpretty(self, node, s):
        if node:
            self.__printpretty(node.right, s + "\t")
            print s + node.s
            self.__printpretty(node.left, s + "\t")
        


def parse(s):
    if s is None or len(s) == 0:
        return None
    if len(s) == 1:
        return Node(s)
    root = Node(s)
    root.left = parse(s[:len(s)/2])
    root.right = parse(s[len(s)/2:])
    return root


def is_scrambled(a, b):
    ra = parse(a)
    rb = parse(b)
    ra.printpretty()
    rb.printpretty()
    return ist(ra, rb)

def ist(a, b):
    if a is not None and b is not None and a.s == 'eat' and b.s =='tae':
        print a.left.s, b.left.s
        print ist(a.left, b.right)

    if a is None or\
       b is None or\
       (len(a.s) == len(b.s) == 1 and a.s != b.s) or\
       len(a.s) != len(b.s):
        return False

    if (ist(a.left, b.left) and ist(a.right, b.right)) or\
       (ist(a.left, b.right) and ist(a.right, b.left)) or\
       a.s == b.s or\
       a.s == b.right.s + b.left.s:
        return True

    return False



    

# BETTER VERSION
def is_scrambled2(a, b):
    if len(a) != len(b):
        return False
    if a == b:
        return True

    d = defaultdict(int)
    for i in range(len(a)):
        d[a[i]] += 1
        d[b[i]] -= 1
    if any(d.values()):
        return False

    for i in range(1, len(a)):
        al = a[:i]
        ar = a[i:]
        bl = b[:i]
        br = b[i:]
        if is_scrambled2(al, bl) and is_scrambled2(ar, br):
            return True
        bl = b[:len(a)-i]
        br = b[len(a)-i:]
        if is_scrambled2(al, br) and is_scrambled2(ar, bl):
            return True

    return False





print is_scrambled2('great', 'rgtae')
print is_scrambled('great', 'rgeat')
print is_scrambled2('great', 'rgeat')
