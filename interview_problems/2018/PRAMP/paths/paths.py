"""
start at bottom left of grid, need to get to upper right
  return # of paths
  don't cross diag


n == 1
  1

(0 0)  ==> (n-1 n-1)



1) bf
    (n-1) + (n-1) moves to get to corner
    try all combos of NEW, take what works
    3^{(n-1) + (n-1)}


2) 

we're in (i, j)


if i and j are n-1, done +1
if off map (if j is too big), done, 0
if above diag, done 0

# norths + # rights

memoize ==> n^2



###############

above diag:
  3, 1
  4, 3
  r > c

at diag
  2 2
  r == c

below diag
  0 2
  r < c


##############

"""



def num_of_paths_to_dest(n):
  assert n >= 1

  if n == 1:
    return 1

  cache = {}

  def recurse(r, c):
    if (r, c) in cache:
      return cache[r, c]

    if r == n-1 and c == n-1:
      return 1
    elif c >= n:
      return 0
    elif r > c:
      return 0

    result = recurse(r+1, c) + recurse(r, c+1)
    cache[r, c] = result
    return cache[r, c] 

  return recurse(0, 0)


print num_of_paths_to_dest(4)
