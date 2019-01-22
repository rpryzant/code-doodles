# meh...not super happy about this one...




def dfs(candidates, start, end, sofar, result):
    if len(sofar) == end:
        result.append(sofar[:])
        return
    for i in range(start, len(candidates)):
        sofar.append(candidates[i])
        dfs(candidates, i + 1, end, sofar, result)
        sofar.pop()

def combine(n, k):
    res = []
    if k < 1 or n < 1 or k > n:
        return res
    candidates = [x for x in range(1, n+1)]
    sofar = []
    dfs(candidates, 0, k, sofar, res)
    return res
                  
                
print combine(4, 3)









def choose(n, k):
    if k > n or k < 1 or n < 1:
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











