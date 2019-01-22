"""
1 = 1
a

2 = 2
  a
    b

3   num(2) + num(2) + 1 (full)
    a
  c   b

4  num(3) + num(3) + num(2) * num(2)
      a
    b   d
          c

5  num(4) + num(4) + num(3) * num(3) + num(2) * num(2)
       a
     b   e
        d  c

6 2*num(5) + n(4)^2 + n(3^2)



k  2( num(k-1) ) + num(k - 2)^2 + etc until k - (k-i) has already been hit
      a


N = num(n-1) + num(n-1) + sum( num(n-i)^2 until i is something we've already hit)
                                       n-i  <=  i

if n == 1:
  return 1
elif n == 2:
  return 2
elif n == 3:
  return 5
else:
  out = 2 * num(n-1)
  for i in range(2, (n/2) + 1):
     out += num(n-i)**2
  return out


for speedup, memoize that shit!!

"""


def num_trees(n):
    if n <= 0:
        return 0
    
    if   n == 1: return 1
    elif n == 2: return 2
    elif n == 3: return 5
    
    out = 2 * num_trees(n - 1)
    out += sum(num_trees(n - i)**2 for i in range(2, (n/2)+1))

    return out
