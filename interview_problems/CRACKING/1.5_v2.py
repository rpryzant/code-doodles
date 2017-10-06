"""
BLEW THE OLD ONE OUT OF THE WATAH!!!x


safe characters? sentences?

check for zero/one

query tgt
pale  bale   substitution
 q+1  t+1

pale  ple    deletion
q+1    t

pale  palTe  insertion
q      t+1

levenshtein distance: O(qt)

i feel like we can do O(q + t)

make sure query/target differ by 1, pad the shorter

iterate jointly through zip(query, target)   (O(q + t))
  on first dissimilarity
    check query[q+1:] == target[t+1:]  (sub)  O(q +t)
          query[q+1:] == target[t:]    (del)  ""
          query[q:] == target[t+1:]    (ins)  ""
"""

def one_away(query, target):
    assert abs(len(query) - len(target)) <= 1

    for i, (qi, ti) in enumerate(zip(query, target)):
        if qi != ti:
            if query[i+1:] == target[i+1:] or \
               query[i+1:] == target[i:] or \
               query[i:]   == target[i+1:]:
                return True
            else:
                return False

    return True


print one_away('pale', 'pXle')
print one_away('pale', 'ple')
print one_away('pale', 'ppale')
print one_away('pale', 'paleX')
print one_away('pale', 'bake')
