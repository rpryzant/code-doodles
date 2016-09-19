from collections import defaultdict 

# tests whether 3 bottles can sum to k

def k_sum(bottles, k):
    d = defaultdict(lambda: None)
    for b1 in bottles:
        for b2 in bottles:
            if d[-b2] is not None:
                return d[-b2][0], d[-b2][1], b2
            d[b1 + b2 - k] = (b1, b2)
    return None


print k_sum([1,4,45,6,10,8], 22)
