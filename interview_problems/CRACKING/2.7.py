

def find_intersection(n1, n2):
    d = {}
    runner = n1
    i = 0
    while runner != None:
        d[id(runner)] = i
        i += 1
        runner = runner.next
    runner = n2
    i = 0
    while runner != None:
        if d.get(id(runner), False):
            return runner, d[id(runner)], i
        i += 1
        runner = runner.next
    return None
