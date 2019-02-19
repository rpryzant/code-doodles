regex 2


dif is_match(s, p):

i = j = 0

while i < len(s) and j < len(p):
    # star
    if j < len(p) - 1 and p[j + 1] == ‘*’:
        while s[i] == p[j]:
            i += 1
    j += 2
# match
elif p[j] == ‘.’ or s[i] == p[j]:
    i += 1
    j += 1
else:
    return False


if i == len(s) and (
j == len(p) or (j == len(p - 1) and p[j + 1] == ‘*’)):

    return True

return False
