"""
merge all intervals

endpoints negative? 
assume these are valid?
does overlapping include containment? 


1) 
ivals are in a
sort a by start time -- O(n log n)
outgoing = []
tmp = [0]
for ival in a[1:]
   if ival overlaps with tmp
      tmp consumes ival
   else 
      add a copy of tmp to outgoing, set tmp to ival
add leftover tmp to outgoing

(pre sorted)
[1,3],[2,6],[8,10],[15,18]

outgoing
[ [1 6] [8 10]
tmp
[8 15]


"""


def overlaps(a, b):
    return max(a[0], b[0]) <= min(a[1], b[1])

def merge(a, b):
    return [min(a[0], b[0]), max(a[1], b[1])]

def merge_all(a):
    a = sorted(a, key=lambda x: x[0])

    out = []
    tmp = a[0]
    for ival in a[1:]:
        if overlaps(ival, tmp):
            tmp = merge(tmp, ival)
        else:
            out.append(tmp[:])
            tmp = ival
    out.append(tmp[:])
    return out


print merge_all([[1,3],[2,6],[8,10],[15,18]])
