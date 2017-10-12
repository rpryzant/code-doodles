"""
THIS DOESN'T WORK, BUT THE IDEA IS THERE!!!!



1 2 3 7 8 9 10 11 20
        ^    

1 2 7 9 20    len m
    ^

3 8 10 11   len n
  ^

the median of both arrays  index x
     know x = (m + n) / 2

if we start at a point, what do we know and how do we move


1) find insertion point of a[mid] in b (could go other way WLOG)
2) cases:
    if we're at median, done
    if too many elements to right, 
       step right by always moving the elem with smaller right neighbor
    if too many elements to left, 
       step left by always moving the elem with bigger left neighbor

"""
from bisect import bisect_left


def search(A, B):
    med_idx = (len(A) + len(B)) / 2

    def searchR(a, b, al=0, ah=len(a)-1):
        if al > ah:
            return None
        am = (al + ah) / 2
        bi = bisect_left(a, a[am]) - 1
        idx_in_total = am + bi
        if idx_in_total == med_idx:
            return a[am] if med_idx % 2 == 1 \
                else float(max(a[am-1], b[bi-1]) + a[am]) / 2
        elif idx_in_total > med_idx:
            return searchR(a, b, al, am-1)
        else:
            return searchR(a, b, am+1, ah)

    return searchR(a, b) or searchR(b, a)


a = [1,2,7,9]
b = [3,4,8]
print a, b
print sorted(a +  b)
print search(a, b)
