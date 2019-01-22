"""
is_anagram:
   historgram char freqs
   o(n)

matching anagrams? 
   compare histograms O(n)   

O(N^2 k) beause have to visit everything and len k counters

hashing? 
   can't hash dicts
   sum of ord() of unique chars, len of string
      ^ content                    ^ uniqueness

   O(nk) hashing each
   O(1) .values 
"""
from collections import defaultdict

def group_anagrams(a):
    def hash(w):
        char_sum = sum(ord(c) for c in set(w))
        length = len(w)
        return char_sum, length

    d = defaultdict(list)
    for word in a:
        d[hash(word)].append(word)

    return d.values()

test = ["eat", "tea", "tan", "ate", "nat", "bat"]
print group_anagrams(test)
