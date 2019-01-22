"""
I like my solution to this one!

let the size of the subtree rooted at node i be k
    - pick node i w prob 1/k
    - branch left w/prob k_l / k
    - branch right w/prob k_r / k

note that if not left or right than k_l or k_r will be 0


"""


class BTNode:
    def __init__(self, x):
        self.data = x
        self.size = 1
        self.left = None
        self.right = None
        
    def insert(self, x):
        self.size += 1
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


    def pick_random(self):
        if random() < 1.0/self.size:
            return self
        elif self.left and random < self.left.size / self.size:
            return self.left.pick_random()
        else:
            return self.right.pick_random()
