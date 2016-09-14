

def increment(n):
    carry = 1
    for i in range(len(n))[::-1]:
        tmp = n[i] + carry
        n[i] = tmp % 10
        carry = tmp / 10
    if carry:
        n.insert(0, carry)
    return n

print increment([8,2,9])
print increment([9,9,9])
