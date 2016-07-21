# TODO TEST, SOME EXTENSIONS??

from bit_vector import Bitvector
import sys
import math
from random import random

sys.path.append('../utilities')
from utilities import hash

MAX_SEED = 32
BITS_IN_BYTE = 8

class Bloomfilter:

    def __init__(self, hash_count = 4, bytes = 1024):
        # default to 1024 byte bit vector
        self.num_bits = bytes * BITS_IN_BYTE
        self.size = 0
        self.bv = Bitvector(self.size)
        self.hash_count = hash_count
        self.hash_seeds = [int(math.floor(random() * MAX_SEED)) for _ in range(self.hash_count)]

    def __hashes_for_key(self, key):
        return [hash(key, seed) % self.bv.get_size() for seed in self.hash_seeds]

    def add(self, key):
        self.size += 1
        hashes = self.__hashes_for_key(key)
        for h in hashes:
            self.bv.set_one(h)

    def remove(self, key):
        if self.membershipTest(key):
            self.size -= 1
        hashes = self.__hashes_for_key(key)
        for h in hashes:
            self.bv.set_zero(h)

    def false_positive_rate(self):
        prob_bit_zero = (1 - (1.0 / self.num_bits)) ** (self.hash_count * self.size)
        prob_bit_one = 1 - prob_bit_zero
        prob_all_bits_one = prob_bit_one ** self.hash_count
        return prob_all_bits_one


    def membershipTest(self, key):
        hashes = self.__hashes_for_key(key)
        for h in hashes:
            if not self.bv.get(h):
                return False
        # note that returning true here only implies probable membership for the key
        # probabability of false positive is 
        return True



def main():
    bf = Bloomfilter()
    bf.add(5)
    bf.add(12)
    bf.add(1)
    print bf.membershipTest(4)
    print bf.membershipTest(5)
    bf.remove(5)
    print bf.membershipTest(5)
    print bf.false_positive_rate()

if __name__ == "__main__":
    main()
