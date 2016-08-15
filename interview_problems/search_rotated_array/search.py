

def s(a, t, l, h):
    if l > h:
        return -1
    m = (l + h) / 2
    if a[m] == t:
        return m
    if a[h] <= a[l]:
        if t > a[m] or t < a[h]:
            return s(a, t, m + 1, h)
        else:
            return s(a, t, l, m - 1)
    else:
        if t > a[m]:
            return s(a, t, m + 1, h)
        else:
            return s(a, t, l, m - 1)


test = [4,5,6,7,0,1,2]
print s(test, 5, 0, len(test) - 1)
print s(test, 1, 0, len(test) - 1)
print s(test, 10, 0, len(test) - 1)
            
