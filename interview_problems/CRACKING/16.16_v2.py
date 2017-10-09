"""
subsort

            i      j
1 2 4 7 10 11 7 12 6 7 16 18 19
      ^              ^
      m              n


      i     j
1 2 3 7 4 5 6 8 9
      m     n

1) BF
for i in a
   see if a[i+1:] is less than a[i]

  O(n^2)


2) linear? multiple passes? 
     from front:   m is before the first decrease
     from back: n is before the first increase

   find outer bounds (first decrease/increase)
   scan out from this, stopping when appropriate 

   at boundaries
       m-1 is lower than a[m:]
       n+1 is bigger than a[:n+1]

a = [start mid end]

mid is unsorted
so
max(start) < [mid end]
min(end) > [start mid]

1) find seeds
2) shrink i until property above holds
3) grow j until property above holds
"""


def first_drop_idx(a):
    # assumed a is unsorted
    return next( (i for i, x in enumerate(a[:-1]) if a[i] > a[i+1]) )

def first_jump_idx(a):
    # assumed a is unsorted
    return next( (i for i, x in enumerate(a[:-1]) if a[i] < a[i+1]) )

def unsorted_subseq(a):
    # assert unsorted
    i = first_drop_idx(a)
    j = len(a) - first_jump_idx(a[::-1]) - 1
    
    right_min = min(a[i:])
    while max(a[:i]) >= right_min:
        i -= 1

    left_max = max(a[:j+1])
    while min(a[j+1:]) <= left_max:
        j += 1

    return i, j
#                            3              9                   
print unsorted_subseq([1,2,4,7,10,11,7,12,6,7,16,18,19])
