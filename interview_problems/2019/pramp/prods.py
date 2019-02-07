"""
Array of Array Products
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.

Solve without using division and analyze your solution’s time and space complexities.

Examples:

input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]
Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 20
[output] array.integer





given:   [a1,    ,an]
return:  [a2 * ... * an,   prod(a1, a_i-1) * prod(a_i+1, n)        ]

no overflow/underflow


brute force:
  for each number
    loop through the array and prod up everything not that idx
    
    O(n^2)
    
maybe better:
  prod(a1, a_i-1) * prod(a_i+1, n)
  \-------------/
  
  O(n) time
  O(n) space
  
  (1): get left-hand partial products
  (2): work from back, get right-hadn partial products, multiply by what you had before


pseudocode


[2, 7, 3, 4]
 ^
        

RP   168
OUT   [42, 56, 24, 84]


LP  [1, 2, 14, 42, 168]

[84, 24, 56, 42]
 


left_products
right_product (int)
out (can't change)

"""

def array_of_array_products(arr):
  if len(arr) <= 1:
    return []

  left_products = [1]
  for i, x in enumerate(arr):
    left_products.append(left_products[-1] * x)

  out = []
  right_product = 1
  for i in range(len(arr))[::-1]:
    left_product[i + 1] = right_product * left_products[i]
    right_product *= arr[i]

  return left_product[1:][::-1]
