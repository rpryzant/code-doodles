"""
given root of a tree
 => no cycles, only one parent
nodes have non-negative integers 
we want to find the minimal root=>leaf path 
  where "score" of a path is sum along edges
  
  
brute force:
  traverse tree (dfs, bfs), remember sums, return min
  
  dfs = O(L) (l is # leaves)
  bfs = O(L) 


can we do it faster?
  prune branches that we know can't be the min
  
  do dfs
  keep track of min_so_far
  if current_sum > min_so_far:
    give up

           1
       2       50
     30       5   9

PSEUDOCODE

"""

# space: O(D) D = depth
# time:  O(N) N = # nodes

def get_cheapest_cost(root):
  cur_min = int.max

  def recurse(node, sofar):
    sofar += node.cost

    # prune branches bigger than current min
    if sofar > cur_min:
      return
    
    if not node.children:
      cur_min = min(cur_min, sofar)
    else:
      for child in node.children:
        recurse(child, sofar)

  recurse(root, 0)

  return cur_min

########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None
 
