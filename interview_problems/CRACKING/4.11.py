


class BTNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        
    def insert(self, x):
        if x < self.data:
            if not self.left:
                self.left = BTNode(x)
            else:
                self.left.insert(x)
        else:
            if not self.right:
                self.right = BTNode(x)
            else:
                self.right.insert(x)

    def delete(self, x):
        if self.data == x:
            if not self.left:
                self = self.right
            else:
                self.data = self.left.__pop_max()
            return True
        elif self.left and x < self.data:
            return self.left.delete(x)
        elif self.right:
            return self.right.delete()
        else:
            return False

    def __pop_max(self):
        if not self.right:
            out = self.right.data
            self = self.left
            return out
        else:
            return self.right.__pop_max()
            
    def find(self, x):
        if self.data == x:
            return self
        if self.left and x < self.data:
            return self.left.find(x)
        elif self.right:
            return self.right.find(x)
        return None
