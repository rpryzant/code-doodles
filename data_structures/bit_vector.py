import math

BITS_PER_INT = 32
BYTES_PER_INT = 4

class Bitvector:

    def __init__(self, num_bytes = None):
        num_bytes = num_bytes or 64
        num_chunks = (num_bytes + (BYTES_PER_INT - 1)) / BYTES_PER_INT
        self.data = [0 for _ in range(num_chunks)]
        self.size = len(self.data) * BITS_PER_INT

    def __chunk_and_index(self, index):
        chunk_num = index / BITS_PER_INT
        chunk_index = index % BITS_PER_INT
        return (chunk_num, chunk_index)

    def get_size(self):
        return self.size

    def get(self, index):
        chunk_num, chunk_index = self.__chunk_and_index(index)
        mask = 1 << chunk_index
        return (self.data[chunk_num] & mask) != 0

    def set_one(self, index):
        chunk_num, chunk_index = self.__chunk_and_index(index)
        mask = 1 << chunk_index
        self.data[chunk_num] = self.data[chunk_num] | mask

    def set_zero(self, index):
        chunk_num, chunk_index = self.__chunk_and_index(index)
        mask = ~(1 << chunk_index)
        self.data[chunk_num] = self.data[chunk_num] & mask

    def printpretty(self):
        s = ''
        for i, chunk in enumerate(self.data):
            s += '%s. ' % i
            for _ in range(32):
                s += str(chunk & 1)
                chunk >>= 1
            s += '\n'
        print s


def main():
    ba = Bitvector(1)
    ba.set_one(30)
    ba.set_one(0)
    ba.printpretty()
    ba.set_zero(0)
    ba.set_zero(5)
    ba.printpretty()
    print ba.get(30)
    print ba.get(31)

if __name__ == "__main__":
    main()
    





