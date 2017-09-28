# i like this better!!!!!!



def merge(a, b):
    ai, bi = 0, 0
    out = []

    while ai < len(a) and bi < len(b):
        if a[ai] <= b[bi]:
            out.append(a[ai])
            ai += 1
        else:
            out.append(a[bi])
            bi += 1

    out += a[ai:] if ai < len(a) else b[bi]
    return out
