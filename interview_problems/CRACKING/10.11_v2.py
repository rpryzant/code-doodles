"""
not too bad!


5 8 6 2 3 4 6

are we guarenteed he correct # of peaks/vallys?   (yes)
negative numbers? repeats? repeats yes, negs yes
equality == peak?  no


5 8 6 2 3 4 6

make local decisions, swaping adjacent #s until property is reached
   O( n^2 )
   swapping rule?
   correctness guarentees?


get median on first pass (n log n sort :( ) 
get numbers below, numbers above on second pass
lay them out on third pass
   guarenteed correct: all #s below < all #s above so you'll get 
      hills/vallys for sure
   can also check for illegal input: abs(len(below) - len(above)) <= 1
O(n log n) + O(n)space


structure? 
   alternating ==> ~1/2 need to be > the other ~1/2
     ==> use mean? no, could get dragged way out
   

   windows of 3, swap max and min (overlapping by 1 elem) if max is not in middle
      enforces property on a local level
      works on this example..
      but repeats? 
        could shuffle the list in O(n)...but no guarentees
   O(n)


5 8 6 2 3 4 6
5 8 2 6 3 6 4

"""

def swapper(l, favor_fn):
    out = l[:]
    for i in range(len(l) - 2)[::2]:
        triple = l[i : i+3]
        move_to_mid(triple, favor_fn(triple))
        out[i : i+3] = triple
    return out

def move_to_mid(triple, i):
    if i != 1:
        tmp = triple[1]
        triple[1] = triple[i]
        triple[i] = tmp

def peakify(l):
    assert l is not None
    out = swapper(l, lambda l: max((x, i) for i, x in enumerate(l))[1])
    return out if is_peaky(out) else None

test = [5, 8, 6, 2, 3, 4, 6]
print peakify(test)

test = [5,3,1,2,3]
print peakify(test)

