#  ABANDONED / UNFINISHED
# 
# python passes arguments by assignment, so node modification is
# non-trivial. I have to access nodes either by their parents or change
# the nodes' member/instance variables. 
#
# sigh...on to java




class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
        # adding parents because python is annoying and passes arguments by assignment
        self.parent = None


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
                node.left.parent = node
            else:
                self.__insert(node.left, data)
        else:
            if not node.right:
                node.right = Node(data)
                node.right.parent = node
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


    def delete(self, data):
        self.__delete(self.root, data)

    def __delete(self, node, data):
        if not node:
            return
        if node.data == data:
            if not node.right and not node.left:
                node.parent. = None
                return
            else:
                min = self.get_min(node.right)
                min_data = min.data
                self.__delete(node.right, min_data)
                node.data = min.data
                return
        elif data < node.data:
            self.__delete(node.left, data)
        else:
            self.__delete(node.right, data)

    def get_min(self, node):
        if not node.left:
            out = node
            if node.right:
                node = node.right
            return out
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
