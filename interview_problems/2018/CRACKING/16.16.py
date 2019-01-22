# my way:
# binary search for the start, end pos of subsort
#    O(n log n)
#
# their way:
#   think of array as [left, middle, right] where left is sorted, 
#      middle is unsorted, right is unsorted
#   so max(left) should be less than min(middle+right)
#   and min(right) should be more than max(left+middle)
#   
#   init left to longest increasing subseq at start
#   init right to longest decreasing subseq at end
# 
#   shrink left & right until objective properties are satisfied
#
#    O(n)
# 
#      i REALLY like this solution. Important to think of problems in terms 
#       of fundamental properties, min, and max




def fl(a, t, l, h):
    if l > h or l < 0 or h > len(a)-1:
        return None
    m = (l + h)/2
    if m < len(a) - 1 and a[m+1] > t and a[m] <= t:
        return m
    elif a[m] > t:
        return fl(a, t, l, m-1)
    else:
        return fl(a, t, m+1, h)

def find_limits(a):
    m = -1
    for i in range(len(a)):
        tm = fl(a, a[i], 0, i - 1)
        if tm:
            m = tm
            break
    n = -1
    for i in range(len(a))[::-1]:
        tn = fl(a, a[i], i+1, len(a)-1)
        if tn:
            n = tn
            break
    return m, n





def eil(a):
    for i in range(1, len(a)):
        if a[i-1] > a[i]:
            return i-1
    return None

def sds(a):
    for i in range(0, len(a) - 1)[::-1]:
        if a[i+1] < i:
            return i
    return None

def shrinkleft(a, left, minR):
    while a[left] >= minR:
        left -= 1
    return left

def shrinkright(a, right, maxL):
    while a[right] < maxL:
        right += 1
    return right



def find_limits_better(a):
    # find left increasing subsequence
    left = eil(a)
    if left is None:
        return
    # find right increasing subsequence
    right = sds(a)
    #find index of min(middle+right) side
    minR = next((i+left+1 for i, x in enumerate(a[left+1:]) if x == min(a[left:])))
    #index of max(left+middle)
    maxL = next((i for i, x in enumerate(a[:right]) if x == max(a[:right])))

    #shrink left subsequence until max(left) < min(middle, right)
    #shrink right until min(right) < max(middle, left)
    return shrinkleft(a, left, minR), shrinkright(a, right, maxL)


print find_limits([1,2,4,7,10,11,7,12,6,7,16,18,19])
        
print find_limits_better([1,2,4,7,10,11,7,12,6,7,16,18,19])
