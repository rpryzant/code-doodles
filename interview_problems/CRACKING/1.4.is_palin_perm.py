"""
in notes
bf:
   iterate over all permutations, return true if one is palindrome
      O(n! * n)


smart: 
   permutation has pairs of all chars except for MAYBE 1 with 1 or 3 
     ===> more generally, only one char type is allowed to occur an odd num times

   count num chars (except space/punctuation), ret true if <= 1 occurs an odd num times

"""

# O(n) time and space
from collections import Counter
def palin_perm(s):
    c = Counter(s.lower())
    num_odd = 0
    for k in c:
        if k.isalpha() or k.isdigit():
            if c[k] % 2 == 1:
                num_odd += 1
    return True if num_odd <= 1 else False

print palin_perm('Tact Coa')



def toggle(bv, i):
    bv ^= (1 << i)
    return bv


# O(n) time O(1) space
def palin_perm_better(s):
    bv = 0
    for c in s.lower():
        if c.isalpha():
            bv = toggle(bv, ord(c) - ord('a'))
    return bv & (bv - 1) == 0

print palin_perm_better('Tact Coa')
