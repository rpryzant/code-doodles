


def add(A, B):
    if not A or not B:
        return None
    Ap = Bp = 0
    carry = 0
    C = ""
    while Ap < len(A) or Bp < len(B):
        if Ap < len(A) and Bp < len(B):
            tmp = carry + int(A[::-1][Ap]) + int(B[::-1][Bp])
        else:
            tmp = carry + int(A[::-1][Ap]) if Ap < len(A) else int(B[::-1][Bp])
        C = C + str(tmp & 1)
        carry = (tmp & 2) >> 1
        Ap += 1
        Bp += 1
    if carry == 1:
        C = C + str(carry)
    return C[::-1]



print add("11", "1")
