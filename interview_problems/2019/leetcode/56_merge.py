merge intervals


are intervals sorted? 

if yes:
    O(n) space + time

a
----------
            -------------


def overlaps(a, b):
    return max(a) < min(b) or max(b) < min(a)

def merge(a, b):
    return [min(a[0], b[0]), max(a[0], b[0])]

def merge(arr):
    out = arr[0]
    for ival in arr[1:]
if overlaps(out[-1], ival):
    out = out[-1:] + merge(out[-1], ival)
else:
    out += [ival]
    return out


if no:
sort ( O(n log n) ) + prev ( O(n) )

---      ----      ----
 ----

dict with special hash function


