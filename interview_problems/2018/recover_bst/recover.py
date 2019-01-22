# pretty cool solution - find nodes out-of-order via the in order traversal





def in_order(n):
    if not n:
        raise StopIteration
    for x in in_order(n.left):
        yield x
    yield n
    for x in in_order(n.right):
        yield x


def find_pair(n):
    prev = None
    saved = None
    for x in in_order(n):
        if not prev:
            prev = x
        else:
            if n.d < prev.d:
                if not saved:
                    saved = (prev, n)
                else:
                    saved[1] = n
    return saved


def recover_tree(n):
    swap = find_pair(n)
    if swap is None:
        return
    tmp = swap[0].d
    swap[0].d = swap[1].d
    swap[1].d = tmp

