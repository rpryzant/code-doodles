# python passes arguments by assignment, so node modification is
# non-trivial. I have to access nodes either by their parents or change
# the nodes' member/instance variables. 





class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

    def no_children(self):
        return self.left is None and self.right is None

    def has_both_children(self):
        return self.left is not None and self.right is not None


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


    def dfs(self, data):
        return self.__bfs(self.root.left, data) or self.__bfs(self.root.right, data)

    def __dfs(self, node, data):
        if not node:
            return None
        elif node.data == data:
            return node
        else:
            return self.__bfs(node.left, data) or self.__bfs(node.right, data)


    def delete(self, data):
        self.__delete(None, self.root, False, data)

    def __delete(self, parent, current, is_left, data):
        if not current:
            return
        elif current.data is data:
            if current.no_children():
                if is_left:
                    parent.left = None
                else:
                    parent.right = None
            elif current.has_both_children():
                min = self.get_min(current)
                self.delete(min)
                current.data = min
            elif current.right:
                if is_left:
                    parent.left = parent.left.right
                else:
                    parent.right = parent.right.right
            else:
                if is_left:
                    parent.left = parent.left.left
                else:
                    parent.right = parent.right.left
        elif current.data > data:
            self.__delete(current, current.left, True, data)
        else:
            self.__delete(current, current.right, False, data)

    def get_min(self, node):
        if not node:
            return None
        if not node.left:
            return node.data
        else:
            return self.get_min(node.left)

    def printpretty(self):
        self.__printpretty(self.root, "")

    def __printpretty(self, node, s):
        if node:
            self.__printpretty(node.right, s + "\t")
            print s + str(node.data)
            self.__printpretty(node.left, s + "\t")        
        


b = BST()
b.insert(5)
b.insert(11)
b.insert(3)
b.insert(4)
b.insert(12)
b.insert(2)

b.printpretty()

b.delete(5)

b.printpretty()
