"""
classic case of pairs

[package1 package2 .. package n]
weight limit

need to select 2 packages whose sum == limit

only 1 pair
[3 1]  [1 3]

1) bf
  for package, check all others, if sum == limit, return that pair
  O N^2

2)
21

[4, 6, 10, 15, 16]
    ^
    if we find a 21-6=15 later on, we're done
    {
      needed: index
    }
64

for package in arr:
  if package val in my bf
    O(n) to recover that

  mark (target - package)

O(n) time
O(n) space

21
[4, 6, 10, 15, 16]
            ^
{
  17: 0
  15: 1
}

negatives are allowed, not limits

arr = []

"""
class BV:
  def __init__(self, limit):
    self.vec = [0 for _ in (limit+1)/32]

  def get_bit()

  def set_bit()


def get_indices_2(arr, limit):
  bv = BV(limit)
  for i, p in enumerate(arr):
    if bv.get(p) == 1:
      # search arr[:i] for limit - p

    else:
      bv.set(limit - p)


def get_indices_of_item_wights(arr, limit):

  d = {}
  for i, weight in enumerate(arr):
    if weight in d:
      return i, d[weight]
    else:
      d[limit - weight] = i

  return []

