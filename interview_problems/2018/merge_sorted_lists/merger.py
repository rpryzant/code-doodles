


def merge_build(a,b):
    c = []
    ai = bi = 0
    while ai < len(a) and bi < len(b):
        if a[ai] <= b[bi]:
            c.append(a[ai])
            ai += 1
        else:
            c.append(b[bi])
            bi += 1
    if ai < len(a):
        return c + a[ai:]
    else:
        return c + b[bi:]



a = [1,5,8]
b = [2,2,2,9]
print merge_build(a,b)
