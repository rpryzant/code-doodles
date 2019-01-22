

def convert(d):
    out = []
    while d > 0:
        out.append(int(d * 2))
        d = (d * 2) % 1
    return '0.' + ''.join(str(x) for x in out)



print convert(0.75)
print convert(0.25)
print convert(0.625)
