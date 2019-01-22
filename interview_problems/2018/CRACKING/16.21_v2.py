"""
bada bing, bada boom


sum swap

given two arrays of ints, find pair of vals (one from each) 
that you can swap to give teh arrays the same sum


[4 2 1 1 1 2]       [3 6 3 3]


all positive?  yes
length 1 allowed? (tfivial)
invalid solutions allowed? always guarenteed a win? YES


1) bf
     try all pairs of numbers O(nm)


2) linear time
A                   B     
[4 1 2 1 1 2]       [3 6 3 3]
sum:   12              15

sum_dif = 11 - 15 = -4

first pass through A, you can learn how much you still need from b

A { 
    4: need 6
    1: need 3
    2: need 4
    x: need x - (sum_dif / 2)

s_dif = 4
       +2
B { 
    3: 1
    6: 4

NOTE: 
if sum_dif % 2 == 1: 
   not possible


ALGO

sum_dif = sum(A) - sum(B)
assert sum_dif % 2 == 0

for x in A:
  d[x - (sum_dif / 2)] = x

for x in B:
  if x in d:
     return x

reutrn None
"""



def sum_swap(A, B):
    sum_dif = sum(A) - sum(B)
    assert sum_dif % 2 == 0
    
    d = {x - (sum_dif / 2): x for x in A}
    for x in B:
        if x in d:
            return x, d[x]
    return None


print sum_swap([4, 2, 1, 1, 1, 2], [3, 6, 3, 3])
