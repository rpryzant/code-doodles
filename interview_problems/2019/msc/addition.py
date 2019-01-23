





def get_digit(l, i):
    if i == len(l):
        return 0, i
    else:
        return int(l[-(i+1)]), i + 1

def add(a, b):
    ai, bi, carry = 0, 0, 0
    out = []
    while ai < len(a) or bi < len(b) or carry > 0:
        a_digit, ai = get_digit(a, ai)
        b_digit, bi = get_digit(b, bi)

        print(a_digit, b_digit, carry)

        tmp = a_digit + b_digit + carry
        out.append(str(tmp % 10))
        carry = tmp // 10

    return int(''.join([str(x) for x in out[::-1]]))



print add('646', '758'), 646+758
