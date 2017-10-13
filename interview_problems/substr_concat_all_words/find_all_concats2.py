"""
s  (len k)
a = [w1, w2, ... wn     (m chars)

find all instances of wwwwww (n, each represented once) in s

what if w == ''? 
    not allowed
are all of these alphanumeric?  yes


1) build O(1) "detector" (n!) via hashing all permutations then apply it to s (k)

2) compare char distributions ( O(1) ) for seed locations, then 
       verify matches with "words" ( O(k) )
   O( k/m )   if i do the comparing right


CHAR DISTRIBUTION HASH COMPARISON
   want two strings to hash to the same number IFF they have the
   same number/type of characters (permutations are OK)
   sum ord()? 
      no, could spill over
   xor them all? 
      also no, could have too many collisians
   sum hash(char)?
      yes!!!

"""

def find_concats(s, a):
#    assert stuff!

    meta_hash = lambda str: sum(hash(ch) for ch in str)

    detector = meta_hash(''.join(a))
    total_len = sum(len(w) for w in a)

    for i in range(len(s) - total_len):
        substr = s[i : i + total_len]
        if meta_hash(substr) == detector:
            if all([w in substr for w in a]):
                yield i

print [x for x in find_concats("barfoothefoobarman", ["foo", "bar"])]
