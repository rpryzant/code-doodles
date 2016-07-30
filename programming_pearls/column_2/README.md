
* Finding all anagrams of a given word. Hash the word by serializing a histogram of word counts (`O(n)` time, `O(1)` space). Then encode each word in the dictionary (`O(|D|n)` where `n` is the longest word in the dictionary) in a similar way and look for matching encodings. If you could spend some time/space proproccessing, I'd sort the dictionary encodings so that I can find anagrams with a `log|D|` binary search.

* Finding duplicates in large sorted file of ints. Preprocess: find min (`O(1)`), max (`O(1)`), mid (probe around middle of file...worst case `O(n)` but realistically `O(1)`) element. Binary search on list with active set = half of list with more numbers.  `O(log n)`.

* See rotation.c