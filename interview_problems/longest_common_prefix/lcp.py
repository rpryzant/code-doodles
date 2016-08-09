# the trie solution is faster (each character is only visited once) but also more costly in terms of space
# it's also more flexible (finds longest of any type prefix...not just common.
#           to make it common, do a quick check in get_lcp() to make sure self.children has only 1 element



def brute_force_lcp(s):
    lcp = ''
    i = 1
    while all(map(lambda x: lcp in x, s)):
        lcp = s[0][:i]
        i += 1
    return lcp[:-1]


class Node:
    def __init__(self, ch = None):
        self.children = []
        self.ch = ch

    def insert(self, s):
        if not s:
            return
        child = next((x for x in self.children if x.ch is s[0]), None)
        if child:
            child.insert(s[1:])
        else:
            new = Node(s[0])
            self.children.append(new)
            new.insert(s[1:])
            
    def get_lcp(self):
        prefixes = map(lambda x: x.get_longest_run(), self.children)
        max = 0
        max_prefix = None
        for prefix in prefixes:
            if len(prefix) > max:
                max = len(prefix)
                max_prefix = prefix
        return max_prefix
            
    def get_longest_run(self):
        return self.__get_longest_run('')

    def __get_longest_run(self, s):
        if len(self.children) != 1:
            return s + self.ch
        return self.children[0].__get_longest_run(s + self.ch)

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        self.root.insert(s)

    def get_lcp(self):
        return self.root.get_lcp()


def smart_lcp(s):
    t = Trie()
    for si in s:
        t.insert(si)
    return t.get_lcp()




test = ['hillo', 'hiboop', 'hi']
print brute_force_lcp(test)
print smart_lcp(test)

test = ['hillo', 'hiboop', 'hi', 'believe', 'bell']
print brute_force_lcp(test)
print smart_lcp(test)
