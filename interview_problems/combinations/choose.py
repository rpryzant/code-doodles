# meh...not super happy about this one...

def choose(n, k):
    if k > n:
        return
    # init ptrs
    ptrs = [i for i in range(k)]
    # while not done (first ptr is far enough from the back)
    while ptrs[0] <= n - k:
        i = len(ptrs) - 1
        # give the value of all ptrs in their starting positions
        yield [x+1 for x in ptrs]
        # send each pointer towards the back, yielding combinations as you go
        while i > 0:
            for j in range(ptrs[i] + 1, n - ((len(ptrs) - 1) - i)):
                ptrs[i] = j
                yield [x+1 for x in ptrs]
            i -= 1
        # increment first ptr and reset the rest
        ptrs[0] += 1
        for j in range(i+1, k):
            ptrs[j] = ptrs[j-1] + 1


for l in choose(4, 3):
    print l
