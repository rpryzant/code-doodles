
# abstracted to disallowing n dups
def rm_dups_ii(l, n):
    i = 0
    c = 1
    while i < len(l) - 1:
        c = c + 1 if l[i] == l[i + 1] else 1
        if c > n:
            del l[i + 1]
        else:
            i += 1
    return l, len(l)

print rm_dups_ii([1,1,1,1,1,1], 3)
print rm_dups_ii([1,1,1,2,2,3], 2)
print rm_dups_ii([1,1,1,2,2,3, 3,3,3], 2)
