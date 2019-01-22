# i like my soln to this one!
# even though it's O(n) space
# still O(n) time


def trap(a):
    if not a:
        return -1
    m = [a[-1]]
    for i in range(len(a) - 1)[::-1]:
        m.append(max(m[-1], a[i]))
    s = 0
    left_edge = 0
    for x in a:
        right_edge = m.pop()
        if x >= left_edge:
            left_edge = x
        else:
            s += min(left_edge, right_edge) - x
    return s

print trap([0,1,0,2,1,0,1,3,2,1,2,1])
                 
