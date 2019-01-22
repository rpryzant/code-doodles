#TODO FINISH111111111

import re

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ptrs = []

    def add(self, w):
        self.root.add(w)
        
    # returns lens of all si's that have been found
    def step(self, c):
        done = []
        i = 0
        while i < len(self.ptrs):
            self.ptrs[i] = self.ptrs[i].step(c)
            if not self.ptrs[i]:
                del self.ptrs[i]
            else:
                if self.ptrs[i].is_leaf():
                    done.append(self.ptrs[i].depth())
                i += 1
        return done
    def __str__(self):
        return str(self.root)

    
class TrieNode:
    def __init__(self, x = None):
        self.ch = x
        self.children = []
        
    def add(self, w):
        if not w:
            return
        if not self.ch:
            self.ch = w[0]
            start = 1
        else:
            start = 0
        if any(map(lambda x: x.ch == w[start], self.children)):
            for child in self.children:
                if child.ch == w[start]:
                    child.add(w[start:])
                    return
        else:
            self.children.append(TrieNode(w[start]))
            self.children[-1].add(w[start:])

    def is_leaf(self):
        return self.children is []

    def step(self, c):
        for child in children:
            if child.ch == c:
                return child
        return None

    def __str__(self):
        print "*******"
        for x in self.children:
            print x.ch
        print "*******"
        return '%s' % self.ch + '\n\t'.join(str(x) for x in self.children)

def find_all_better(b, T):
    t = Trie()
    for s in T:
        t.add(s)

    print t

    starts = []
    for i, ch in enumerate(b):
        starts += map(lambda x: x - i, t.step(ch))
    return starts
    








def find_all(b, T):
    return [next((match.start() for match in re.finditer(si, b))) for si in T]

b = "hello my name is reid"
T = ["ell", "ame", "rei"]
print find_all(b, T)
print T
print find_all_better(b, T)
