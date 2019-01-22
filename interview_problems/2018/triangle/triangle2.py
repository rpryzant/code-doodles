# -*- coding: utf-8 -*-
"""
negatives? 
guarenteeed well formed triangle?
just sum, or whole path? (just sum)


1
enumerate all paths (dfs)
take max


2
dijkstras?


3
some kind of dp thing?


def gen_path_sums
use dp to traverse this tree

def max sum
iteratively update max (to save on space)
"""

import sys
def min_sum(t):

    def gen_path_sums(r, c, sofar):
        if r >= len(t):
            yield sofar
            return

        for left_sum in gen_path_sums(r+1, c, sofar + t[r][c]):
            yield left_sum

        for right_sum in gen_path_sums(r+1, c+1, sofar + t[r][c]):
            yield right_sum

    min_sum = sys.maxint
    for path_sum in gen_path_sums(0, 0, 0):
        min_sum = min(path_sum, min_sum)

    return min_sum


test = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print min_sum(test)

