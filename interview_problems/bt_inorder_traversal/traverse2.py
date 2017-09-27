
class Node(object):
    def __init__(self, v):
        self.right = None
        self.left = None
        self.v = v


def traverse(n):
    if n is None: 
        raise StopIteration

    for x in traverse(n.left):
        yield x

    yield n.v

    for x in traverse(n.right):
        yield x
