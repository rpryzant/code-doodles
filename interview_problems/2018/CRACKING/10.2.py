# i like my solution to this, but had some trouble getting the indexes right. be careful, Reid!
# in notes

def group_anagrams(A):
    Ap = sorted([(sorted(w), i) for i, w in enumerate(A)], key = lambda x: x[0])
    for i, (char_array, index) in enumerate(Ap):
        Ap[i] = A[index]
    return Ap


print group_anagrams(['hello', 'good','doog', 'olelh'])
