
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









def can_decode(pair):
    return 10 <= int(pair) and int(pair) <= 26

def num_ways(M):
    cache = {}
    def nw(i):
        if cache.get(i, False):
            return cache[i]
        if i == 0 and M[0] == '0' or i < 0:
            cache[i] = 0
        elif i == 0:
            cache[i] = 1
        else:
            cache[i] = nw(i-1) + (1 if M[i-1] != '0' and can_decode(M[i-1:i+1]) else 0)

        return cache[i]
    
    return nw(len(M) - 1)





print num_ways('')
print num_ways('123')
print num_ways('12')
print num_ways('99999')
print num_ways('12022')
print num_ways('0')
print num_ways('100')
