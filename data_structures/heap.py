



def heap:
    def __init__(self):
        self.data = []


    def push(self, x):
        self.data.append(x)
        self.siftUp()

    def pop(self, x):
        out = self.data[0]
        self.data = self.data[1:]
        self.swap(0, len(self.data) - 1)
        self.siftDown()
        return out

    def siftUp(self):
        # takes the last element in the heap and swaps it up
        # to wherever it belongs
        i = len(data) - 1
        while(i > 0 and self.valAt(i) < self.parentVal(i)):
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def siftDown(self):
        # swaps down first element to wherever it belongs
        i = 0

        while self.left(i) < len(self.data):
            lefti = self.left(i)
            righti = self.right(i)

            if righti >= len(self.data) or self.data[lefti] < self.data[righti]:
                child = lefti
            else:
                child = righti

            self.swap(i, child)
            i = child
            

    def swap(self, i, j):
        tmp = self.data[j]
        self.data[j] = self.data[i]
        self.data[i] = tmp

    def valAt(self, i):
        return self.data[i]

    def parentVal(self, i):
        return self.data[self.parent(i)]

    def parent(self, i):
        return (i - 2) / 2

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return i * 2 + 2




