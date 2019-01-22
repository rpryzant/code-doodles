

def rm_dups(x):
    def hash_list(l):
        return sum(hash(li) for li in l)
    out = []
    hashes = set()
    for subset in x:
        h = hash_list(subset)
        if h not in hashes:
            out.append(subset)
            hashes.add(h)
    return out



def subsets(x):
    out = []
    
    def subsetR(sofar, remaining):
        if remaining == []:
            out.append(sofar)
        for i in range(len(remaining)):
            subsetR(sofar[:], remaining[i+1:])
            sofar.append(remaining[i])
            subsetR(sofar[:], remaining[i+1:])
            sofar.pop()

    subsetR([], x)
    return rm_dups(out)



print subsets([1,2,3])
