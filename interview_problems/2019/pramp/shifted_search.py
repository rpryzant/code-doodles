"""
sorted array
shifted LEFT by x places

1 2 3 4 5
3 4 5 1 2

given shiftArr
given num

find num in shiftArr

COULD BE FULLY SHIFTED
No dups
No guarentees on length


IF it wasn't shifted
  => bs

IF you knew k (shifting number)
[a_1    a_k   a_k+1      a_n ]
    all of the a_i (i <=k) is bigger than a_k+1

[big half | small half]
          k

brute force:
  find k (linear scan)   <====
  bs on the correct half (log n)

a little better
  BS to find k           ====
  BS on the correct half
  
if were at i
  i == k if a[i] > a[i + 1]
  move right if a[i] > a[-1]    
  move left if a[i] < a[0]


[9, 12, 17, 2, 4, 5]
              
              ^            k = arr.length - 1                  
              
              
====================
[9, 12, 17, 2, 4, 5], num = 2, k = 2
        k
                     hi
                     
[ 1 2 3 4 5 ]  
7


====================

"""


def find_k(arr, lo, hi):
  if hi == 0:
    return len(arr)\
  m = (lo + hi)   // 2
  if arr[m] > arr[m + 1]:
    return m
  elif arr[m] > arr[-1]:
    return find_k(arr, m + 1, hi)
  else:
    return find_k(arr, lo, m -1)

def search(arr, num):
  # find k
  k = find_k(arr, 0, len(arr) - 1)
  # search top or bottom
  if k == len(arr):
    return binary_search(arr, 0, len(arr) - 1, num)
  elif num >= arr[0] and num <= arr[k]:
    return binary_search(arr, 0, k, num)
  else:
    return binary_search(arr, k+1, len(arr) - 1, num)



def shifted_arr_search(shiftArr, num):
  pass # your code goes here
