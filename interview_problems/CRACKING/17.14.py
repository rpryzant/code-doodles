# in notes


class MaxHeap:
    def __init__(self, k):
        self.a = []
        self.k = k
        
    def swap(self, i, j):
        tmp = self.a[i]
        self.a[i] = self.a[j]
        self.a[j] = tmp

    def insert(self, x):
        if len(self.a) < self.k:
            self.a.append(x)
            self.__percolate(len(self.a)-1)
        elif x < self.a[0]:
            self.a[0] = x
            self.__heapify(0)

    def __percolate(self, i):
        while i > 0 and self.a[i] > self.a[(i-1)/2]:
            self.swap(i, (i-1)/2)
            i = (i-1)/2

    def __heapify(self, i):
        while i < len(self.a):
            if (i * 2) + 1 < len(self.a) and self.a[i] < self.a[(i*2) + 1]:
                self.swap(i, (i*2) + 1)
                i = (i * 2) + 1
            elif (i * 2) + 2 < len(self.a) and self.a[i] < self.a[(i * 2) + 2]:
                self.swap(i, (i * 2) + 2)
                i = (i * 2) + 2
            else:
                return


def smallest_k(a, k):
    if k > len(a) or k < 1:
        return None
    h = MaxHeap(k)
    for x in a:
        h.insert(x)
    return h.a


test = [34,7,34,2,4,7,700,3,36,76,1,1,57,8,5,345,3]

print smallest_k(test, 3)
