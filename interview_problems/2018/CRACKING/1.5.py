

def first_disagreement(a, b):
    if len(a) < len(b):
        a += '*'
    elif len(a) > len(b):
        b += '*'
    return next((i for i, (ai, bi) in enumerate(zip(a, b)) if ai != bi))

def is_oneoff(a, b):
    i = first_disagreement(a, b)
    if len(a) < len(b):
        a = a[:i] + b[i] + a[i:]
    elif len(a) > len(b):
        a = a[:i] + a[i + 1:]
    else:
        a = a[:i] + b[i] + a[i+1:]
    if all(map(lambda (x,y): x==y, zip(a, b))):
        return True
    return False


print is_oneoff('pale', 'ple')
print is_oneoff('pales', 'pale')
print is_oneoff('pale', 'bale')
print is_oneoff('pale', 'bake')
