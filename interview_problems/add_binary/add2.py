"""
start by being careful about a, etc, etc

i think this is a stronger solution, makes the structure more obvious

"""


def xor(b1, b2):
    return 0 if b1 == b2 else 1

def band(b1, b2):
    return 1 if b1 == b2 else 0


def add(a, b):
    carry = 0
    out = []
    i = 0
    while i < len(a) or i < len(b) or carry > 0:
        ai = int(a[::-1][i]) if i < len(a) else 0
        bi = int(b[::-1][i]) if i < len(b) else 0
        if sum([ai, bi, carry]) == 3:
            carry = 1
            out.append('1')
        elif sum([ai, bi, carry]) == 2 :
            carry = 1
            out.append('0')
        elif sum([ai, bi, carry]) == 1:
            carry = 0
            out.append('1')
        elif sum([ai, bi, carry]) == 0:
            carry = 0 
            out.append('0')
        i += 1

    return out[::-1]

print add('11', '1')
