# -*- coding: utf-8 -*-
# MUCH BETTER THAN LAST YEAR!!!
# but  not correct because need to find unused lcm, not arbitrary lcm
"""
5!
120

9!
962880

12!
479001600

14!
..00

15!
..000

19!
..000

20!
..0000


25!
..000000

trailing zeros come from 
(5 * 2)’s
10’s



1 brute force
compute n!
while n % 10 == 0; c+=1; n /= 10







2: fives and tens
n! = n (n-1) (n-2) … (1)
       (multiple of 10)..  (multiple of 5)   .. (2) ..
10!
10
5,2
20!
10
5,2
20
15
25
5
10
15
20
25
count number of 5’s, add extra if power of five?
what’s actually going on here?
n! is decomposed into products of 10’s
25! = (2*5) * 10 * (4*15) * (20) * (8*25) * other stuff
10      10     60      20      200
and then we can read off the 0’s!!!!!!!!


for each multiple of 5 < n
get trailing 0’s from lcm(that multiple, 10)
add zeros to running total
"""

from fractions import gcd

def trailing_zeros(x):
    out = 0
    while x > 0 and x % 10 == 0:
        out += 1
        x /= 10
    return out

def lcm(a,b):
    return abs(a * b) / gcd(a, b)

def factorial_zeros(n):
    out = 0
    for x in range(n+1)[::5][1:]:
        print x, trailing_zeros(lcm(x, 10)), lcm(x, 10)
        out += trailing_zeros(lcm(x, 10))
    return out

print factorial_zeros(25)
print factorial_zeros(24)



