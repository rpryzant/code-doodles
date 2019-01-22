# better soln gives end locations...to make it start make trienodes remember their depth

import re

class Trie:
    def __init__(self):
        self.roots = []
        self.ptrs = []

    def add(self, w):
        for root in self.roots:
            if root.ch == w[0]:
                root.add(w[1:])
                return
        self.roots.append(TrieNode(w[0]))
        self.roots[-1].add(w[1:])
        
    # returns lens of all si's that have been found
    def step(self, c):
        done = False
        i = 0
        while i < len(self.ptrs):
            self.ptrs[i] = self.ptrs[i].step(c)
            if not self.ptrs[i]:
                del self.ptrs[i]
            else:
                if not self.ptrs[i].children:
                    done = True
                i += 1
        for root in self.roots:
            if root.ch == c:
                tmp = root
                self.ptrs.append(tmp)
        return done

    def __str__(self):
        for root in self.roots:
            print root.ch
            for child in root.children:
                print "\t%s"% child.ch
                for chh in child.children:
                    print "\t%s"% chh.ch

        return '\n'.join(str(root) for root in self.roots)

    
class TrieNode:
    def __init__(self, x = None):
        self.ch = x
        self.children = []
        
        
    def add(self, w):
        if not w:
            return
        for child in self.children:
            if child.ch == w[0]:
                child.add(w[1:])
                return
        self.children.append(TrieNode(w[0]))
        self.children[-1].add(w[1:])

    def step(self, c):
        for child in self.children:
            if child.ch == c:
                return child
        return None

    def __str__(self):
        return self.ch

def find_all_better(b, T):
    t = Trie()
    for s in T:
        t.add(s)
    print t
    starts = []
    for i, ch in enumerate(b):
        if t.step(ch):
            starts += [i]
    return starts
    






def find_all(b, T):
    return [next((match.start() for match in re.finditer(si, b))) for si in T]

b = "hello my name is reid"
T = ["ell", "ame", "rei"]
print find_all(b, T)
print T
print find_all_better(b, T)
