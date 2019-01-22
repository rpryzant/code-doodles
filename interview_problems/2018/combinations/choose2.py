"""
does order matter? no
so we want the binomial


n^k

fuck yeah!


"""



def choose(n, k):
    assert k <= n
    out = set()

    def recurse(remaining, sofar):
        if len(sofar) == k:
            return sofar[:]

        for i, x in enumerate(remaining):
            sofar.append(x)
            new = recurse(remaining[i+1:], sofar)
            if new:
                out.add(tuple(new))
            sofar.pop()

    recurse(range(1, n+1), [])
    return list(out)


print choose(4, 2)
