"""




n 
11000000000000000000000

m
10011

i = 2 
j = 6

10000000000000
            --
1001100

"""


# make inverted mask with whole where we want to insert
# then shift insertion number into hole and stick it in
# and this mask with n to clear out non-set bits of m in insertion area
# finally or "shifted m" with n to insert m's bits
def insert_bits(n, m, i, j):
    n &= ~((2**(j-i+1)-1) << i) | (m << i)
    return n | (m << i)



print insert_bits(2**10, 19, 2, 6)
