
# i like my solution to this one!
# O(n) t + s




def num_ways(A):
    cache = {}
    def NW(i):
        if cache.get(i, None):
            return cache[i]
        if i == 0:
            cache[i] = 1
        else:
            cache[i] = NW(i - 1)
            if can_decode(A[i-1: i+1]):
                cache[i] += 1
        return cache[i]

    return NW(len(A) - 1)


def can_decode(pair):
    return 10 <= int(pair) and int(pair) <= 26


print num_ways('12')

print num_ways('9999')

print num_ways('1222')
