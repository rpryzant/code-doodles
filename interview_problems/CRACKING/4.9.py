# i like my solution to this one!!


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sequences(n):
    if not n:
        return []
    subsequences = [a+b for a in sequences(n.left) for b in sequences(n.right)] +\
                   [b+a for a in sequences(n.left) for b in sequences(n.right)]
    if subsequences:
        map(lambda x: x.insert(0, n.data), subsequences)
    else:
        subsequences.append([n.data])
    return subsequences
    


root = Node(2)
root.left = Node(1)
root.right = Node(3)

superRoot = Node(4)
superRoot.right = Node(5)
superRoot.left = root

print sequences(root)
print sequences(superRoot)
