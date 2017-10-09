"""
OTHER SOLN WAS CLEANER, BUT THIS ONE IS MORE DURABLE I THINK


x = amount to consume
n = random number
      = number of bottleso

repeats allowed? no
negatives? no
multiple picks? no
return true/false? indices? values?


1) bf
    try all combinations
    n^3

2) dfs + early stopping
   also n^3


3) multi passes?
   
pass 1:
 on visiting each elem, you know **how much left you have**

{first pass elem:
    {second pass elem:
        how much remains
    }
}
O(n^2) time    because need to search dict for remainder
O(n^2) space  
hmm...how can we improve this


=== pass 1
{how much remains after 1st pass:    first pass elem}
{how much remains after 2nd pass: (2nd pass elem, first pass key)}  
     (N-1 of these for each key of 1st dict)
on third pass, if "2nd pass dict" has this elem, recover
O(n^2) time
O(n^2) space


"""
from collections import defaultdict

def drinks(a, x):
    remainder_lookup = {}
    for i, ai in enumerate(a): 
        for j, aj in enumerate(a[:i] + a[i+1:]):
            if x - ai - aj > 0:
                remainder_lookup[x - ai - aj] = i, j

    for i, ai in enumerate(a):
        if i not in remainder_lookup.get(ai, [i]):
            return True
    return False


print drinks([ 1, 4, 45, 6, 10, 8 ], 22)

