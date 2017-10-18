# -*- coding: utf-8 -*-
"""
given
r1 r2 … rn

return 
c1 c2 … cn

where
ri = child i’s rating
ci = number of candies assigned to child i
all ci > 0
ci > ci+1 if ri > ri+1
ci > ci-1 if ri > ri-1



1 brute force:
put ratings in sorted stack
give each child one candy O(n)
iterate through ratings, and give children with that
rating an extra candy

O(n^2) (n unique ratings worst case)


2 looking at examples
<<
 2 3 4 3 2 2 1 
[1 2 5 3 2 2 1]
 1 2 3 2 1 1 0
>>
 min | max
want min in some parts, max in othes

get l>r and r>l perspectives
if see 1, set to 1
if i+1 > i, increase by 1
if i+1 < i, decrease by 1


iterate left-> right:
if on incline, take left=>right bound
l>r describes min
if on decline, take right=>left bound
r>l describes min
if at peak, take max


O(n)


1 2 3 4 5 1 3 4

4 3 1 5 4 3 2 1
2 1 

 1 2 4 3 2 2 0
[1 2 5 3 2 2 1]

left => right
if see increase, count += 1
if see decrease
if 1, set to 1
if i < i+1, set to 1
set to count-1
if count hits 0
correct before (add 1 until first decrease from left)
set to 1
O(n^2)!!! 


{ rank: [indices where it ocurs] }   N space
sort keys (N log N)
loop through in ascending order, jumping to index and setting to min
"""
from collections import defaultdict

def candy(ranking):
    out = [1] * len(ranking)
    d = defaultdict(list)
    for i, r in enumerate(ranking):
        d[r].append(i)

    for rank in sorted(d.keys())[1:]:
        for idx in d[rank]:
            if idx == 0:
                out[idx] = 1 if ranking[idx] < ranking[idx+1] else out[idx+1] + 1
            elif idx == len(ranking) - 1:
                out[idx] = 1 if ranking[idx] < ranking[idx-1] else out[idx-1] + 1
            else:
                if ranking[idx] < ranking[idx-1] and ranking[idx] < ranking[idx+1]:
                    out[idx] = 1
                else:
                    out[idx] = max(out[idx-1], out[idx+1]) + 1
    return out

print candy([4,2,3,4,1])
print candy([5,4,3,2,1])
print candy([1,1,1])
print candy([1,4,4,4,3])

