import math

def find_common_ancestor_with_parent_ptr(a, b):
    dif = depth(a) - depth(b)
    forward, lagging = (a, b) if dif < 0 else (b, a)
    for _ in math.abs(dif):
        lagging = lagging.parent
    while id(forward) != id(lagging) and all([forward, lagging]):
        forward = forward.parent
        lagging = lagging.parent
    if not forward or not lagging:
        return None
    return forward
