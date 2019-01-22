# i prefer this!!!

def JG(a):
    cache = {}

    def recurse(i):
        if i in cache:
            return cache[i]

        if i == len(a) - 1:
            cache[i] = True
        elif i > len(a) - 1 or a[i] == 0:
            cache[i] = False
        else: 
            cache[i] = any([recurse(i+j+1) for j in range(a[i])])
        return cache[i]

    return recurse(0)

print JG([2,3,1,1,4])
print JG([3,2,1,0,4])

