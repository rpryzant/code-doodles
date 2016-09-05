

def make_hv(a):
    a = sorted(a)[::-1]
    vp = len(a) - 1
    for i, x in enumerate(a):
        if not i % 2 and not is_hill(a, i):
            swap(a, i, len(a) - 1)
        if i % 2 and not is_valley(a, i):
            if a[vp] <= a[-1]:
                swap(a, i, vp)
            else:
                swap(a, i, len(a) - 1)
            vp -= 1
    return a

def is_hill(a, i):
    if (i == 0 and a[i] > a[i+1]) or (i == len(a) - 1 and a[i] > a[i-1]):
        return True
    if (a[i] > a[i-1]) and (a[i] > a[i+1]):
        return True
    return False



def is_valley(a, i):
    if (i == 0 and a[i] < a[i+1]) or (i == len(a) - 1 and a[i] < a[i-1]):
        return True
    if (a[i] < a[i-1]) and (a[i] < a[i+1]):
        return True
    return False


def swap(a, i , j):
    tmp = a[j]
    a[j] = a[i]
    a[i] = tmp




def make_hv_better(a):
    a = sorted(a)
    for i in range(1, len(a))[::2]:
        swap(a, i, i-1)
    return a


def make_hv_best(a):
    for i in range(1, len(a))[::2]:
        swap(a, i, max_index(a, i))
    return a
def max_index(a, i):
    return next( (j for j in range(i-1, i+2) if a[j] == max(a[i-1:i+2])) )


test = [5,8,6,2,3,4,6]
print make_hv(test)
print make_hv_better(test)
print test
print make_hv_best(test)

test = [5,3,1,2,3]
print make_hv(test)
