
"""

====BF
1) read in /usr/share/dict into hashmap
2) bfs on that
 - structure which gives all words 1 edit distance away


====BETTER?
1) read words into trie





===bfs
 1) method that gives all possible successors (done under the hood somehow)
 2) bfs on that (bidirectional)

"""
from Queue import Queue

class WordList:
    def __init__(self, l):
        self.words = [x.strip().lower() for x in open('/usr/share/dict/words') if len(x.strip()) == l]

    def get_successors(self, w):
        return [word for word in self.words if len(word) == len(w) and self.distance(word, w) == 1]
        
    def distance(self, a, b):
        return len(a) - sum(int(a[i] == b[i]) for i in range(len(a)))


def BiBFS(startA, startB, wList):
    qA = Queue()
    vA = {startA: 1}
    qA.put(startA)

    qB = Queue()
    vB = {startB: 1}
    qB.put(startB)


    while not qA.empty() or qB.empty():

        xA = qA.get()
        for succ in wList.get_successors(xA):
            if succ in vB:
                return vA[xA] + vB[succ] - 1
            vA[succ] = vA[xA] + 1
            qA.put(succ)

        xB = qB.get()
        for succ in wList.get_successors(xB):
            if succ in vA:
                print xB, succ
                return vB[xB] + vA[succ] - 1
            vB[succ] = vB[xB] + 1
            qB.put(succ)

    return -1


def ladder(seed, end):
    if len(seed) != len(end):
        return -1

    wList = WordList(len(seed))

    return BiBFS(seed, end, wList)

    


print ladder('hit', 'cog')
