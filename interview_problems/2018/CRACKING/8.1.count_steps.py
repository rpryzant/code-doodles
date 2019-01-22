

 

def cs2(n, l):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif l[n] != -1:
        return l[n]
    else:
        l[n] = cs2(n - 1, l) + cs2(n - 2, l) + cs2(n - 3, l)
    return l[n]

print cs2(50, [-1 for _ in range(51)])
