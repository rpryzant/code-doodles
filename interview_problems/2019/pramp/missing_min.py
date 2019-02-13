"""
given: arr (unique positive integers (including 0))
produce: minimum number NOT in arr

 [0, 1, 2, 3]  => 4 
 [1, 2, 4, 0]  => 1
           ^
1

initialize candidate at 0
if sorted:
  loop through array,
    keep track of candidate min
    if find someting smaller (or equal) than candidate_min, incriment
    if find something bigger, you're done
  
1 ≤ arr.length ≤ MAX_INT
0 ≤ arr[i] ≤ MAX_INT for every i, 0 ≤ i < MAX_INT

bute force:
(1)
sort array, find first gap
  O(n log n)

(2)
use aux arr to toggle bits for nums in arr
read off first 0 from bitmask
O(n + MAX_INT) time
O(MAX_INT) space

(3)
on one pass: min, max
[11111111101111111111100101010111]   bitmask
          ^   


initialize candidate at 0
if sorted:
  loop through array,
    keep track of candidate min
    if find someting smaller (or equal) than candidate_min, incriment
    if find something bigger, you're done

"""
  
  
# first attempt: O(n log n) time, O(1) space
def get_different_number(arr):
  for i in range(len(arr) - 1):
    if abs(a[i] - a[i+1]) > 1:
      return a[i] + 1
  return a[-1] + 1

  c = 0
  
  
  [1, 2, 0, 3, 4] => 5
  
  [0, 1, 3, 4, 5]  
        ^
    
  [0, 1, 2, 3, 4]


  # loop through arr in increasing order
  for x in sorted(arr):
    if x == c:
      c += 1
    else:
      return c
  
  return c


