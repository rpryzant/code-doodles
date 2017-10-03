# i prefer this, simpler and still works O(n)


def plan_trip(g, c):
    assert len(g) == len(c)

    deltas = [gi - ci for gi, ci in zip(g, c)]
    
    # trip is impossible
    if sum(deltas) < 0:
        return -1

    maxi = -1
    max = 0
    cur = 0
    for i, delta in enumerate(deltas[::-1] + [deltas[-1]]):
        if delta < 0:
            cur = 0
        else:
            cur += delta
            if cur > max:
                max = cur
                maxi = i % len(deltas)  # account for that last transition
    out = len(deltas) - maxi - 1
    return out

# deltas = [1,-1,0]
# iter is [0, -1, 1, 0]


print plan_trip([5,2,1],[4,3,1])
print plan_trip([5,5,5], [1,1,13])
print plan_trip([1,2],[2,1])
print plan_trip([5, 5,5,5,5,5,5], [-8,-4,0,-7,-5,-5,2])
