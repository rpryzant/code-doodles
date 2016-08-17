from Queue import Queue

class Node:
    def __init__(self, p):
        self.project = p
        self.children = []

    def adopt(self, n):
        self.children.append(n)

    def disown(self, n):
        for i, child in enumerate(self.children):
            if child.project == n:
                del self.children[i]

    def __str__(self):
        return self.project

def init_table(projects):
    root = Node('*')
    d = {}
    for project in projects:
        d[project] = Node(project)
        root.adopt(d[project])
    return d, root

def make_tree(projects, dependancies):
    d, root = init_table(projects)
    for dependancy in dependancies:
        root.disown(dependancy[0])
        d[dependancy[1]].adopt(d[dependancy[0]])
    return d, root

def gen_order(d, root):
    out = []
    q = Queue()
    for child in root.children:
        q.put(child)
    while not q.empty():
        n = q.get()
        if n.project not in out:
            out.append(n.project)
            for c in n.children:
                q.put(c)
    return out    

def make_plan(p, d):
    d, root = make_tree(p, d)
    print root.project, [str(x) for x in root.children]
    for k in d:
        print k, [str(x) for x in d[k].children]


    order = gen_order(d, root)
    if len(order) != len(p):
        print order
        return None
    return order

p = ['a','b','c','d','e','f']
d = [('d','a'),('b','f'),('d','b'),('a','f'),('c','d')]
print make_plan(p,d)
