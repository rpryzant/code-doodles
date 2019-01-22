"""
4 5 6 7 2 4 5 20 28 2 4 5 9 34 2 34 

profit = distance from local max to nearest local min

biggest profit = biggest vally => hill path

1 always hold min
2 increase potential profit as you go (replace max if needed)
3 if you come across a new min, reset everything

O(n) space + time
"""

import sys

def buy_sell(a):
    start = 0
    max_coords = [-1, -1]
    for i, price in enumerate(a[1:]):
        if price <= a[start]:
            start = i+1
        if price - a[start] > a[max_coords[1]] - a[max_coords[0]]:
            max_coords = [start, i+1]

    return max_coords


print buy_sell([1,5,3,2,10,49,1,4,8]), [1,5,3,2,10,49,1,4,8]
print buy_sell([6,5,4,3,2,1])
print buy_sell([1,1,1,1, 6])



