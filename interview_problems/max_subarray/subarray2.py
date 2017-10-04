# slightly cleaner implementation, but i peeked at the answer oops!


def max_subarray(a):
    tmpsum = 0
    tmpcoords = [None, None]
    maxsum = 0
    maxcoords = [None, None]
    for i, x in enumerate(a):
        if x + tmpsum < 0:
            tmpcoords[0] = i+1
            tmpsum = 0
        else:
            tmpcoords[1] = i
            tmpsum += x
            if tmpsum > maxsum:
                maxsum = tmpsum
                maxcoords = tmpcoords[0], i
    return maxsum, a[maxcoords[0] : maxcoords[1]+1]    


print max_subarray([-2,1,-3,4,-1,2,1,-5,4])
