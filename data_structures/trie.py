"""
Implementation of a trie
- this isn't very compressed...inits 26 blank children for each node.
       TODO init as you go!

"""

import Queue

ANYTHING = '.'


class TrieNode:
    def __init__(self, letter):
        self.children = [None for _ in range(26)]
        self.letter = letter.lower()
        
    def contains(self, letter):
        letter = letter.lower()
        return any(map(lambda x: False if x is None else x.letter == letter, self.children))

    def insert(self, letter):
        letter = letter.lower()
        self.children[self.__char_to_index(letter)] = TrieNode(letter)

    def child_for_letter(self, letter):
        letter = letter.lower()
        return self.children[self.__char_to_index(letter)]

    def get_children(self):
        return [x for x in self.children if x is not None]

    def __char_to_index(self, c):
        return ord(c.lower()) - ord('a')

    def pp(self):
        print '%s -> %s' % (self.letter, ','.join(c.letter for c in self.get_children()))


class Trie:
    def __init__(self):
        self.root = TrieNode(ANYTHING)

    def insert(self, word):
        self.__insert(self.root, word)

    def __insert(self, node, word):
        if not word:
            return
        if not node.contains(word[0]):
            node.insert(word[0])
        self.__insert(node.child_for_letter(word[0]), word[1:])

    def contains(self, word):
        return self.__contains(self.root, word)
    
    def __contains(self, node, word):
        if not word:
            return True
        if not node.contains(word[0]):
            return False
        return self.__contains(node.child_for_letter(word[0]), word[1:])

    def pp(self):
        q = Queue.Queue()
        q.put(self.root)
        while not q.empty():
            n = q.get()
            n.pp()
            for c in n.get_children():
                q.put(c)




def main():
    t = Trie()
    t.insert('test')
    t.insert('tepid')
    t.pp()
    print t.contains('Test')
    print t.contains('test')
    print t.contains('text')

if __name__ == '__main__':
    main()
