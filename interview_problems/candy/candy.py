"""

   r1   r2     ...    rN

   c1   c2     ...    cN


   -all ci must get AT LEAST 1 candy
   -


   1 2
   1 2*
   1 1



1)
   sort & remember recovery index O(n log n) time, O(n) space
   iterate through sorted, check whether assigned to neighbors akready   O(n) space
      give smallest rating possible  


2)
    iterate through unsorted
    check neighbors
    if smaller than both, give 1 candy
    if bigger than i-1, give 1 more candy than i-1
    if bigger than i+1, 
    

 1 4 4 4 3
 1 2   2 1



    [4, 2, 3, 4, 1]
     2  1  2  2  1

"""



def candy(ratings):
    if not ratings:
        return 0
    s_ratings = sorted([(r, i) for i, r in enumerate(ratings)], key=lambda x: x[0])
    assignments = {}
    candies = 0

    for (rating, i) in s_ratings:
        left = assignments.get(i-1, None)
        left_peak = 0 if not left else left[1] - 1 if left[0] == rating else left[1]

        right = assignments.get(i+1, None)
        right_peak = 0 if not right else right[1] - 1 if right[0] == rating else right[1]

        assignments[i] = rating, max(left_peak + 1, right_peak + 1)

    return sum([x[1] for x in assignments.values()])

print candy([4,2,3,4,1])
print candy([5,4,3,2,1])
print candy([1,1,1])
print candy([1,4,4,4,3])














