

def max_subarray(a):
    maxsum = 0
    maxcoords = None
    tmpsum = 0
    tmpcoords = [-1, -1]
    for i, x in enumerate(a):
        if x < 0 and tmpsum > maxsum:
            maxsum = tmpsum
            maxcoords = tmpcoords[:]
        if tmpsum + x <= 0:
            tmpsum = 0
            tmpcoords = [i+1, -1]
        else:
            tmpsum += x
            tmpcoords[1] = i
    if tmpsum > maxsum:
        maxsum = tmpsum
        maxcoords = tmpcoords
    return maxsum, a[maxcoords[0] : maxcoords[1] + 1]


print max_subarray([-2,1,-3,4,-1,2,1,-5,4])
