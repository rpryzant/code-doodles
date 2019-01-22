"""
check if rotation, using only one call to isSubstring()

waterbottle
erbottlewat erbottlewat

how large are these strings?
are they guarenteed to be permutations of each otehr?
are they both rotated? or just one?

1 
relax constraints
keep rotating and call isSubstring() at each step
O(n) (n^2) technically because strings are immnubable)
problem: multiple calls

2
ok, so replace isSubstring() with a proxy (e.g. hash)
O(n)
but i think there’s a hint with that method name

3
find “rotation point”
1
hash all increasing seqs of str1
and find biggest seq in str2 that maps to a key
O(n) space :( 

2
chomp from
start of s1
end of str1
track hashes as you go, first time they match
is a potential fit, then verify
by undoing rotation and calling isSubstring()
O(n^2) also technically but basically O(n)

4
holy SHIT you can just paste them!!
O(n) space, constant time!
"""


def is_rotation(s1, s2):
    return isSubstring(s1, s2 + s2) and len(s1) == len(s2)

