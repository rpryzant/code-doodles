

# c is ((x1, y1), (x2, y2))
def volume(c):
    return (c[1][0] - c[0][0]) * min(c[0][1], c[1][1])

# greedy search from outside in, always moving inwards from the limiting side
def gen_containers(a):
    l = 0
    r = len(a) - 1
    while l < r:
        yield ((l, a[l]), (r, a[r]))
        if a[l] <= a[r]:
            l += 1
        else:
            r -= 1


def find_largest_container(a):
    maxvol = 0
    maxcon = None
    for c in gen_containers(a):
        if volume(c) > maxvol:
            maxvol = volume(c)
            maxcon = c
    return c


print find_largest_container([1,1])
print find_largest_container([3,2,1])
