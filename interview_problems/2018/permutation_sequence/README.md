## Problem

The set `[1,2,3,…,n]` contains a total of `n!` unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):
```
"123"
"132"
"213"
"231"
"312"
"321"
```
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.


## A Neat Solution


Let's start off by looking at an example. Let's look at the 4th element
in the sequence of permutations of `[1,2,3]`
```
1 2 3
1 3 2
2 1 3
2 3 1  **
3 1 2
3 2 1
```
Well it's apparent that we're going to be selecting elements from 
   an array `a = [1,2,3]` to build each permutation. After we select
   an element, it's done - the only other elements that remain valid
   for selection are the other elements in a. So we can delete
   each selected element from a. 

We can also think of each permuation in terms of each element's index
   in a. 

The above two observations/ideas can be combined. The permuation `"1 2 3"`
   becomes `"0 0 0"`, because:
       - 1 is the 0th element of `a = [1,2,3]`
       - 2 is the 0th element of `a = [2, 3]`
       - 3 is the 0th element of `a = [3]`

Let's apply this translation to all of the ordered permuations of `[1,2,3]`:
```
0 0 0
0 1 0
1 0 0
1 1 0
2 0 0 
2 1 0
```
Now all we need to do is look up the right indices for permuation k and 
   we're done! But how to do that...It's evident that we're going to be
   building these indices one element at a time. So for a permuation
   element i, how do we get the ith index?

Well, it seems like in each column the indices are chunked up into
   "blocks" of repeated digits. The size of those blocks shrink
   from column to column. E.g. for column 1: 

````
0 0 0   block 0, block digit: 0
0 1 0

1 0 0   block 1, block digit: 1
1 1 0

2 0 0   block 2, block digit: 2 
2 1 0
```
Note that the size of a block is len(a) - 1. We can come up with 
quick formulas for finding the block number and, given a block number,
     what digit it corresponds to:
```
  block num = how many blocks can fit into k? 
            = (k - 1) / (len(a) - 1)!
   bring back   ^             ^ size of each block = num inner permutations of a 
  to 0-indexing                                    = num permuataions of a after an element is removed
                                                   = (len(a) - 1)!
```
```
  block digit = what index of a[] does block "block num" correspond to?
              = block num % len(a)
```
So the digit we want to add to the outgoing permuation is
```
    a[block digit] = a[block num % len(a)
                   = a[((k - 1) / (len(a) - 1)!) % len(a)]
```
There's one problem we need to watch out for. When there is one element
   left in a we will be dividing by 0 to get the block num. All we need to do,
   then, is stop iteration a little early. When there's only one element left 
   in a, add that element straight to the outgoing permuation.


Note that there's a practical problem with this solution which precludes its usefullness on large inputs. In order to compute the next permution for a number with `n` digits, we need to be able to compute `(n-1)!`. This isn't a computational problem (we can compute factorials in `O(n)` time with DP). But we might have trouble *storing* that number: the factorial function grows very, very quickly. Even if we had an unsigned 128-bit long, the biggest `(n-1)` we'd be able to handle would be 34. 
