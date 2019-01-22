

def traverse(n):
    def tr(n):
        if n is None:
            raise StopIteration

        for x in tr(x.left):
            yield x

        yield n

        for x in tr(n.right):
            yield x

    return [x for x in tr(n)]
