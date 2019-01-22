

# this is a subproblem of question 4.12

# given a list of numbers, how many contiguous sublists sum to a target value?


#O(n) time and space
from collections import defaultdict

def countSums(l, t):
    d = defaultdict(list)
    runningSum = 0
    out = 0

    for i, x in enumerate(l):
        runningSum += x
        d[runningSum].append(i)

        if runningSum - t in d:
            out += len(d[runningSum - t])

    return out
