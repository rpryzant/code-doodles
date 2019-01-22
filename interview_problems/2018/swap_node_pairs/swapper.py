# in notes

class ll:
    def __init__(self):
        self.root = None

    def append(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.root.append(data)

    def __str__(self):
        return str(self.root)

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

    def append(self, num):
        new = Node(num)
        while self.next:
            self = self.next
        self.next = new

    def __str__(self):
        s = ''
        while self:
            s += "%s => " % self.val
            self = self.next
        return s

def swap_pairs(ll):
    n = ll.root
    #kick off iteration by swapping first pair
    if n.next:
        tmp = n.next
        n.next = n.next.next
        tmp.next = n
        ll.root = tmp
    while n.next is not None and n.next.next is not None:
        prev = n
        n = n.next
        tmp = n.next
        n.next = tmp.next
        tmp.next = n
        prev.next = tmp


# TODO get workign w/in my node framework
def swap_pairsR(ll):
    ll.root = swap_pairsRh(ll.root)

def swap_pairsRh(head):
    if head is None or head.next is None:
        return head
    newhead = head.next
    head.next = swap_pairsRh(newhead.next)
    newhead.next = head
    return newhead


# THIS is the best soln
def swap_pairs_simple(ll):
    #kick off iteration by tacking on additional 'prev'
    n = ll.root
    ll.root = n.next
    p = Node(0)
    to_del = p
    p.next = n
    while p.next and p.next.next:
        t = p.next
        p.next = p.next.next
        t.next = p.next.next
        p.next.next = t
        p = p.next.next
    to_del.next = None

    

        

n = ll()
n.append(1)
n.append(2)
n.append(3)
n.append(4)
print n
swap_pairs(n)
print n
swap_pairs_simple(n)
print n

n = ll()
n.append(1)
print n
swap_pairs(n)
print n


n = ll()
n.append(1)
n.append(2)
n.append(3)
print n
swap_pairs(n)
print n
