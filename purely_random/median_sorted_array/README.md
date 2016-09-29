

Wanted to try out a cool solution to the median of sorted arrays problem I found on http://www.lifeincode.net/programming/leetcode-median-of-two-sorted-arrays-more-elegant-solution/

The problem is as follows:

There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).



The solution is pretty cool. Consider 
'''
A = [a0, ..., ai, ai+1, ..., am-1]
B = [b0, ..., bj, bj+1, ..., bn-1
'''

Now fix `i` and `j` such that `i + j + 2 = k`. Now, if the left part of `A` is less than the right part of `B` and visa versa, then the `k`th element will be either `ai` or `bj`! In other words we are trying to make these properties true
```
A[i] <= B[j+1]
B[j] <= A[i+1]
```

And what if they aren't true? If `A[i] > B[j+1]` then `i` is too big and we need to send it downwards (thus increaing `j` since the two are tied). Likewise, if `B[j] > A[i+1]`, then send `j` downwards (increasing i). 

I've sketched out some quick high level code for this, but haven't fully fleshed out the code (e.g. what happens when `i = 0`?) because I just crashed my bike and my toe is bleeding/hurts so can't really focus.