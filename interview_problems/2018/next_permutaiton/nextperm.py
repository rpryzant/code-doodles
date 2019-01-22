

"""
123
132
213
231
312
32144  # worry about later


158476531

1) element that breaks descending gets flipped with start of descent
     (sometimes)

1 element:
   already done
2 elements:
   if ascending, you can swap
3 elements (n elements):
   if all descending: return [::-1]
   elif [1:] is descending, 
       swap next biggest with front (starting search at end, then backwards)
 
       reverse rest that's NOT a dup of the new


   else work on [1:]

FUCK. YES. 


"""



def nextPerm(a):
    def swap(i, j, l):
        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp
        return l

    # base case a = 1 elem
    if len(a) == 1:
        return a
    # base case a is a pair
    if len(a) == 2 and all(a[i] < a[i+1] for i in range(len(a)-1)):
        return a[::-1]
    # base case a is at the limit
    descendings = [a[i] > a[i+1] for i in range(len(a)-1)]
    if all(descendings):
        return a[::-1]
    
    if all(descendings[1:]):
        i = next((i for i, x in enumerate(a[1:-1]) if a[i+1+1] <= a[0])) + 1
        swap(0, i, a)
        a[1:] = a[1:][::-1]
        return a

    return [a[0]] + nextPerm(a[1:])

print [1,5,8,4,7,6,5,3,1]
print nextPerm([1,5,8,4,7,6,5,3,1])


print nextPerm([1,2,3])
print nextPerm([3,2,1])
print nextPerm([1,2,1])
