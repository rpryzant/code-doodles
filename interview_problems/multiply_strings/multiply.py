

# pre: b is digit < 10
def multiply_by_digit(a, b):
    if int(b) > 9:
        return None
    out = 0
    carry = 0
    for i in range(len(a))[::-1]:
        tmp = int(a[i]) * int(b)
        out += ((tmp % 10) + carry) * (10 ** (len(a) - i - 1))
        carry = tmp/10
    return out

def multiply(a, b):
    out = 0
    for i in range(len(b))[::-1]:
        product = multiply_by_digit(a, b[i])
        out += product * (10 ** (len(b) - i - 1))
    return out

print multiply('153', '123'), 153*123
print multiply('15322', '123'), 15322*123
print multiply('12', '99'), 12*99
