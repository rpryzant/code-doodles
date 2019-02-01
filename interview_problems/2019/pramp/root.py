"""
Root of Number
Many times, we need to re-implement basic functions without using any standard library functions already implemented. For example, when designing a chip that requires very little memory space.

In this question we’ll implement a function root that calculates the n’th root of a number. The function takes a nonnegative number x and a positive integer n, and returns the positive n’th root of x within an error of 0.001 (i.e. suppose the real root is y, then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).

Don’t be intimidated by the question. While there are many algorithms to calculate roots that require prior knowledge in numerical analysis (some of them are mentioned here), there is also an elementary method which doesn’t require more than guessing-and-checking. Try to think more in terms of the latter.

Make sure your algorithm is efficient, and analyze its time and space complexities.

Examples:

input:  x = 7, n = 3
output: 1.913

input:  x = 9, n = 2
output: 3
Constraints:

[time limit] 5000ms

[input] float x

0 ≤ x
[input] integer n




square(x) = y such that y * y = x
root(x, 2) = y

root(x, r) = y
  =>  y ^ r = x
      y * ... * y = x

root(x, r)
  root(7, 3) = 1.9 * 1.9 * 1.9 = 7
  root(9, 2) = 3

root(x, r) = y
  y ^ r = x
  y ^ (r - 1) = x / r
  
BRUTE FORCE
root(x, 1): x
root(x, 2): square(x)
root(x, 3): smaller than square(x)


(1) BRUITEST OF BRUTE FORCE THINGS
for y_hyp  in range(0, square root of x, 0.001):
  is y_hyp ^ n ~ x:
    return y_hyp

(2)
  y \in [0, square(x)]
  
  root(9, 2) = 3    x = 9, r = 2, y = 3  
x = 9, r = 2, y = ?

O(log X)


root(lo, hi, r, y_hyp):
  tmp = y_hyp ^ r:
  if tmp ~ x:
    return y_hyp

  elif tmp < x:
    increase y_hyp
    
  else:
    decrease y_hyp
"""



def pow(x, n):
  out = 1
  for _ in range(n):
    out *= x
  return out


  
def root(x, r):
  lo, hi = 0, x
  y_hyp = (lo + hi) / 2
  x_hyp = pow(y_hyp, r)

  while abs(x_hyp - x) > 0.001:
    if x_hyp > x:
      lo = (lo + y_hyp) / 2
    else:
      hi = (y_hyp + hi) / 2

    y_hyp = (lo + hi) / 2
    x_hyp = pow(y_hyp, r)

  return y_hyp


print(root(9, 2))

