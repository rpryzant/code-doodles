# damn...another problem that busted me up...
# 
# the key to this one is that IF the array were in sorted order
#  AND the array was dense (no solution) then every a[i] would be at 
#  the i-1th position. E.g. [1,2,3,4] has no solution.
# so you swap elements to get them into an approximation of that dense form
#  and then scan through. the first place where a[i] != i-1 is 
#  your golden number!!
#
# O(n) in two passes. even though there's a while loop in that
#    first bit, each number is only going to be swapped once



def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def find(a):
    for i in range(len(a)):
        while (a[i] > 0 and a[i] < len(a)) and (a[i] != i + 1):
            swap(a, i, a[i] - 1)
    for i in range(len(a)):
        if a[i] != i+1:
            return i+1
    return -1

print find([3,4,-1,1])
print find([1,2,0])
