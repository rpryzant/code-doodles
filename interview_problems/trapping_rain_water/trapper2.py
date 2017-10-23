# MY FIRST SOLN WAS BETTER!!!!!!

"""
allowed negatives? 
no
 what happens with edges? 
 not ok

0,1,0,2,1,0,1,3,2,1,2,1


#####

##

###

####

##

#####

###

###


BF
for each spot, find the max level it can be
= min(max to left, max to right)
O(n^2)

better
1st pass: 
from right: lay down highest seen so far
from left: lay down highest seen so far

2nd pass:
sum up  min(highest from right, from left) - a[i]
if you’re not on in an edge-type situation

O(n)
O(n) space
"""





def get_peaks(a):
    out = []
    for i, x in enumerate(a):
        if not out or x > out[-1]:
            out.append(x)
            out.append(out[-1])
            return out

def get_first_peak(adj):
    try:
        return next(
            (i for i in range(len(adj_both)) \
                 if adj[i] == adj[i+1]))
    except StopIteration:
        return -1

def trapper(a):
    adj_r = get_peaks(a)
    start_r = get_first_peak(adj_r)

    adj_l = get_peaks(a[::-1])[::-1]
    start_l = get_first_peak(adj_l)

    adj_both = zip(adj_r, adj_l)

    return sum(min(adj_both[i]) - a[i] for i, x in a[start_r : -start_l]))



