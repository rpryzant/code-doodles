
* Finding all anagrams of a given word. Hash the word by serializing a histogram of word counts (`O(n)` time, `O(1)` space). Then encode each word in the dictionary (`O(|D|n)` where `n` is the longest word in the dictionary) in a similar way and look for matching encodings. If you could spend some time/space proproccessing, I'd sort the dictionary encodings so that I can find anagrams with a `log|D|` binary search.

* Finding duplicates in large sorted file of ints. Preprocess: find min (`O(1)`), max (`O(1)`), mid (probe around middle of file...worst case `O(n)` but realistically `O(1)`) element. Binary search on list with active set = half of list with more numbers.  `O(log n)`.

* See rotation.c - I only did the first algorithm. *TODO*: do the reversal algorithm. Pseudocode:
```
V = AB    // len(A) = rotation distance
compute ArB 
compute ArBr
compute r(ArBr) = BA
```

* Not interested in this problem

* abc => cba pseudocode:
```
V = ABC
compute ArBC
compute ArBrC
compute ArBrCr
compute r(ArBrCr) = CBA
```

* Implementing a phone push-button contact book. 
  * **First idea.** Preprocess the given dictionary of names. Put them all in a trie (implement soon?). The first time a user presses a button, open a new path at each letter the button could stand for. When subsiquent buttons are pressed, open 3 new paths at each existing path head (again one for each letter). When a path becomes unfeasible, trash it. Phone numbers are 7 digits, so there would be a max of 3^7 = 2187 possible paths/duplicates. It would take 7 (3^7) space because each path has to remember itself (possible improvement = node sharing paths). But at the end of the day these are (large) constants, so this solution is `O(7) = O(1)` time and `O(n)` space because of the trie. Downside of this soln is that it'd be harder to code up.
  * **Second idea.** This one is pretty straightforward. The sequence of numbers you'd have to push to get the name *is* that name's encoding. Go through the dictionary, encode each name, then sort the dictionary. Duplicates will be adjacent. Binary search to find entries. This is `O(n log n)` time because of the sort. It might be advantageous because you could sort the dictionary in place, but I still prefer my 1st soln. It takes `O(log n)` time to insert into a sorted list, but essentially `O(1)` for the trie. Same with deletion. People leave and join companies all the time.

* Kind of an antique problem...not worth thinking about.  

* `n` real nums, real `t`, int `k`, *does there exist* a `k`-element subset that sums to `t`.
  * **First idea.** All subsets is `O(2^n)`. All `k`-sized subsets is also bounded by `O(2^n)`. Consider all `k`-sized subsets and return first you come across that sums to `t`.
  * **Second idea.** Decompose `t` into powers of 2 and a remainder. Sum together pairs and quadruples and stuff and consider groups of those to get the 2 bit, then try to absorb in remained. Still exponential because have to do all subset on the paired sums but better by a constant factor...it'd be a pain in the ASS to code up though.
  * **Third idea.** The question only asks **if** such a set exists!! NOTE TO SELF: **READ THESE QUESTIONS CAREFULLY.** A `k`-sized subset that sums to `t` can only exist if the `k` smallest elements sum to something at most *t*. So sort the list, sum the bottom *k* elements, and make sure that sum is less than `t`. `O(n log n)`. This is the best solution.

* How many binary searches need to be performed to buy back the time spent on a sort? Cost of `s` linear searches is `sn`. Cost of `s` binary searches is `s log n + n log n`. Set them equal and see when it's worth it. 

* Fill it with water.