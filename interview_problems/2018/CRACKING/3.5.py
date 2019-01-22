

def percolate(sa, sb):
    top = sa.pop()
    done = True
    while len(sa) > 0:
        if top < sa[-1]:
            sb.append(top)
            top = sa.pop()
        else:
            sb.append(sa.pop())
            done = False
    sb.append(top)
    return done

def transfer(sa, sb):
    while len(sa) > 0:
        sb.append(sa.pop())

def sort(s):
    if not s or len(s) < 2:
        return s
    tmp = []
    done = False
    while not done:
        done = percolate(s, tmp)
        transfer(tmp, s)
    return s


print sort([2,5,6,1])
