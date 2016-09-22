
class RankNode:
    def __init__(self, d, left = None, right = None):
        self.left = left
        self.right = right
        self.cnt = 0
        self.d = d
    
    def insert(self, new):
        if new.d <= self.d:
            self.cnt += 1
            if not self.left:
                self.left = new
            else:
                self.left.insert(new)
        else:
            if not self.right:
                self.right = new
            else:
                self.right.insert(new)

    def getRank(self, x):
        return self.__getRank(x, 0)
    
    def __getRank(self, x, c):
        if x == self.d:
            return c + self.cnt
        elif x <= self.d:
            if not self.left:
                return -1
            return self.left.__getRank(x, c)
        else:
            if not self.right:
                return -1
            return self.right.__getRank(x, c + self.cnt + 1)





def track(x, ranker):
    if not ranker:
        ranker = RankNode(x)
    else:
        ranker.insert(RankNode(x))
    return ranker

def getRank(x, ranker):
    if not ranker:
        return -1
    return ranker.getRank(x)

ranker = None

ranker = track(5, ranker)
ranker = track(1, ranker)
ranker = track(4, ranker)
ranker = track(4, ranker)
ranker = track(5, ranker)
ranker = track(9, ranker)
ranker = track(7, ranker)
ranker = track(13, ranker)
ranker = track(3, ranker)

print ranker

print getRank(1, ranker)
print getRank(3, ranker)
print getRank(4, ranker)
