
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.__insert(self.root, data)

    def __insert(self, node, data):
        if data < node.data:
            if not node.left:
                node.left = Node(data)
            else:
                self.__insert(node.left, data)
        else:
            if not node.right:
                node.right = Node(data)
            else:
                self.__insert(node.right, data)


    def bfs(self, data):
        return self.__bfs(self.root.left, data) or self.__bfs(self.root.right, data)

    def __bfs(self, node, data):
        if not node:
            return None
        elif node.data == data:
            return node
        else:
            return self.__bfs(node.left, data) or self.__bfs(node.right, data)


#    def delete(self, data):
## TODO
        


b = BST()
b.insert(9)
b.insert(4)

print b.root.data
print b.root.left.data        
print b.bfs(4).data
