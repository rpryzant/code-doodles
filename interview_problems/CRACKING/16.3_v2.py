"""
(x11, y11) (x21
(x2, y2)
calcualte intersection


does the intersection have to actually be 
   in the segments?
      ====> YES
are points pre-sorted? left => right?
is a up, b down? 
      ====> YES

"""

def intersection(ptsA, ptsB):

    def slope_from_pts(a, b):
        m = float(b[1] - a[1]) / (b[0] - a[0])
        b = -float(a[0] * m) + a[1]
        return m, b

    mA, bA = slope_from_pts(*ptsA)
    mB, bB = slope_from_pts(*ptsB)

    x = -(bB - bA) / (mB - mA)
    y = mA * x + bA

    a1, a2 = ptsA
    b1, b2 = ptsB
    if x > max(a1[0], b1[0]) and x < min(a2[0], b2[0]) \
            and y > max(a1[1], b2[1]) and y < min(a2[1], b1[1]):
        return x, y
    else:
        return None


print intersection(((0, 0), (1, 1)), ((0, 1), (1, 0)))

