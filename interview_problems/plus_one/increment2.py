"""
non-negative number

most sig           least sig
e.g.
[1 2 4 9 9]

want to add 1

decimals? 
limit to list?
each elemnt guarenteed 0<x<10
are elments decimals?

no, each is a whole digit


1) 
listify(numberfy(list)) + 1)
O(n)
O(n)


2) do the addition manually

init carry to first digit
init i one from back

loop from least to most significant, dumping difference into carry as you go
if anything left in carry, add it to front of list (technically O(n) but yaknow...)
"""

def increment2(a):
    carry = 1
    for i in range(len(a))[::-1]:
        tmp = a[i] + carry
        a[i] = tmp % 10
        carry = tmp / 10
    if carry:
        a.insert(0, carry)
    return a


def increment(a):
    a_num = sum(10**i * x for i, x in enumerate(a[::-1]))
    a_num += 1
    out = []
    while a_num > 0:
        out.append(a_num % 10)
        a_num /= 10
    return out[::-1]
    
print increment([8,2,9])
print increment([9,9,9])







