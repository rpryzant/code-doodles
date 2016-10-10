

def intersection(sA, sB):
    if sA == sB:
        return sA[0]

    def eq_from_pts(A, B):
        m = (B[1] - A[1]) * 1.0 / (B[0] - A[0])
        b = A[1] * 1.0 - m * A[0]
        return m, b

    mA, bA = eq_from_pts(*sA)
    mB, bB = eq_from_pts(*sB)

    if mA == mB:
        return None

    x = -(bB - bA) / (mB - mA)
    y = mA * x + bA

    return (x, y) if x >= sA[0][0] and x <= sA[1][0] else None






print intersection(((0, 0), (1, 1)), ((0, 1), (1, 0)))
