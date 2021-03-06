

# do pre-order traversal of both trees, compare strings of visited nodes
#     O(n + m) time AND space
def containsTree1(n1, n2):
    s1 = ""
    s2 = ""

    getOrderString(t1, s1)
    getOrderString(t2, s2)

    return s1.index(s2) != -1

def getPreOrderString(n, s):
    if n is None:
        s += 'X'
        return
    s += n.data + ' '
    getPreOrderString(n.left, s)
    getPreOrderString(n.right, s)


# better: traverse n1 (bigger), and call matchTree
#  each time you find a root of the other tree
# O(1) space, O(n + km) time (where k is the number
#   of times matchTree is called)

def containsTree(n1, n2):
    def contains(n):
        if n is None:
            return False
        elif n.data == n2.data and matchTree(n, n2):
            return True
        return contains(n.left) or contains(n.right)
            
    def matchTree(n, m):
        if n == m == None:
            return True
        elif n == None or m == None:         # if only one is none
            return False
        elif n.data != m.data:
            return False
        return matchTree(n.left, m.left) and matchTree(n.right, n.right)
        


    if n2 is None:
        return None
    return contains(n1, n2)


# VERSION 2!!!!!!!!

## best: do the above but more cleanly (fully recursive)
#    O(n1 * n2), might try matching t2 for every node of t1 (i fucked up the timing 

def isSubtree(tree1, tree2):

    def search(t1, t2):
        if t1.v == t2.v:
            if contains(t1, t2):
                return True
        return search(t1.l, t2) or search(t1.r, t2)

    def contains(t1, t2):
        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None:
            return False
        elif t1.v != t2.v:
            return False
        elif t1.v == t2.v:
            return isSubtree(t1.l, t2.l) and isSubtree(t1.r, t2.r)

        return False

    return search(tree1, tree2)
