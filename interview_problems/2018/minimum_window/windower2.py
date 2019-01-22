
# this is better than my 1st!!!

def window(S, T):
    def span(locs):
        return max(locs.values()) - min(locs.values())

    def valid(locs):
        return all([x > -1 for x in locs.values()])

    def update(m, cur):
        if (valid(cur) and not valid(m)) or (valid(cur) and span(cur) < span(m)):
            return cur
        return m

    cur = {c: -1 for c in T}
    soln = {c: -1 for c in T}

    for i, c in enumerate(S):
        if c in cur:
            cur[c] = i
        soln = update(soln, cur)

    if valid(soln):
        return S[min(soln.values()) : max(soln.values()) + 1]
    return ''

test = 'ADOBECODEBANC'
testt = 'ABC'

print window(test, testt)

