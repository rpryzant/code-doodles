"""

out
denom

while input hasn't hit 0
   if 1 / denom fits in input
      append a 1 to the end of out
      subtract 1/denom from input

   denom <<= 1
"""


def d2b(d):
    assert d < 1 and d >= 0

    out = ''
    denom = 2
    while d > 0:
        if d >= (1.0 / denom):
            out += '1'
            d -= (1.0 / denom)
        else:
            out += '0'
        denom <<= 1
    return '0.%s' % out



def d2b_better(d):
    out = []
    while d > 0:
        out.append(int(d*2))
        d = (d*2)%1
    return '0.' + ''.join(str(x) for x in out)



print d2b_better(0.625)



