"""

arr 

k pos int 


findPairsWithGivenDifference
 => [x, y] : x, y in arr and x - y = k

[0 0 0 0 0 0]
 i     j

x - y = k
x - k = y

          [i j]    [j i]


1) brute force
  
  for i in arr
    for j in arr
       if j - i == k:
         add pair

2) 
d = {}  # {y => x}
for x in arr:
  d[x - k] = x

out = []
for y in arr:
  if y in d:
    out.append([y, d[y]])
return out

distinct indices (due to k=0):
arr = [0], k = 0

[0, 0]

"""

def find_pairs_with_given_difference(arr, k):
  d = {}  # {y => x}
  for x in arr:
    
    if k == 0:
      continue

    d[x - k] = x

  out = []
  for y in arr:
    if y in d:
      out.append([d[y], y])

  return out







