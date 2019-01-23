# -*- coding: utf-8 -*- 

"""
now….what about next permutation?

0123
0132
0213
0231
  1  1
0312
0321   1320   
1023
1032
1203
1230
1302
1320
2013
1032
1
3210

find biggest i such that a[i] < a[i+1]
(we know everything in a[i+1:] is reverse-sorted)
find smallest number bigger than a[i] in a[i+1:] (call that a[j])
swap a[i], a[j]
a[i+1:] is still reverse-sorted 
reverse a[i+1:]
a[i+1:] is now sorted and ready for perm-ing
"""

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def next_perm(seq):
    i = [i for i in range(len(seq)-1) if seq[i] < seq[i+1]][-1]
    j = min( [(x, j+i+1) for j, x in enumerate(seq[i+1:]) if x > seq[i] ])[1]
    swap(seq, i, j)
    seq = seq[:i+1] + seq[i+1:][::-1]
    return seq

print next_perm([0,3,2,1])
