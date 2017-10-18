# in notes

import re

FLOAT_PATTERN = "^\-?\d*\.\d+$"
INT_PATTERN = "^\-?\d+$"
SCI_PATTERN = "^\-?(\d*\.)?\d+e\+\d+$"

def valid(n):
    return re.match("%s|%s|%s" % (FLOAT_PATTERN, INT_PATTERN, SCI_PATTERN), str(n)) is not None



print valid(0.1)
print valid(230.351)
print valid(.1)
print valid(-.1)
print valid('0.1e')
print valid('0.1s')
print valid('s0.1')
print valid(1)
print valid(-9345)
print valid(1.0e15)
print valid(1e25)

