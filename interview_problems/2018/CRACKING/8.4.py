
# in notes

def __subsets(S, B):
    if not S:
        return B
    return __subsets(S[1:], [x[:] + [S[0]] for x in B]) + __subsets(S[1:], [x[:] for x in B])

def subsets(S):
    return __subsets(S, [[]])

print subsets([1,2,3])
