
"""
Two tracking variables ('marked' and 'visited')

visited is to track where each individual search has already been. 
it prevents getting stuck in a cycle or something

marked is to show where both searches have been. it catches
the first time the searches overlap

I need both identifiers because otherwise, when the system comes
across a loop it woudl mistake it for the edge of the opposing search

"""




from Queue import Queue



def mark_and_expand(q):
    if not q.empty():
        tmp = q.get()
        if tmp.marked:
            return True
        tmp.marked = True
        for child in tmp.children:
            if not child.visited:
                child.visited = True
                q.add(child)
    return q


def find_route(a, b):
    aq = Queue()
    a.visited = True
    aq.add(a)
    bq = Queue()
    b.visited = True
    bq.add(b)

    while not aq.empty() and not bq.empty():
        if mark_and_expand(aq):
            return True
        if mark_and_expand(bq):
            return True
    return False
