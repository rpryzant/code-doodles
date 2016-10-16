
"""


Ac = [1 2 ... n]

A = Ac - some k : 1 <= k <= n




getBit(j) is our only window into ai's


A, Ac are NOT sorted



how would I do this without the bit constraint?

     sum(1 ... n) - sum(A) = missing element


hwo does bit constraint ruin stuff?

    can't do sum(A) as easily...
         could add bit-by-bit O(32n) => O(n)
            hard..would prefer not too...
         sum(i ... n) - sum(A) = (1 - ai) + (2 - a2) + ... + (k - 0) + ... + (n - an)
                                                              ^^^^


   0001
   0010
   0100
   0101
   0110
   ...


1/2
1/4
1/8

not a big fan of my solution (slow vs what's in the book)...

"""



def getBit(x, j):
    return (x & (1 << j)) >> j





def findMissingNum(A):

    s = sum(getBit(a, i) * (2 ** i) for i in range(32) for a in A)
    n = len(A) + 1
    return  (n * (n + 1)) / 2 - s



test = [10, 8, 3, 2, 1,4 ,5,6, 7]

print findMissingNum(test)














