# in notes


def add(a, b):
    result = a ^ b
    carry = (a & b) << 1
    while carry > 0:
        tmp = result ^ carry
        carry = (result & carry) << 1
        result = tmp
    return result

print add(1, 1)
print add(5, 6)
print add(5, 11)
