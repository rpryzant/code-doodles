
import re


"""


s = '4 5 + 3 -'

st [-6]

a = 3
b = 9




"""

OPS = {
    '+': lambda (x,y): x+y,
    '-': lambda (x,y): x-y,
    '*': lambda (x,y): x*y,
    '/': lambda (x,y): x*1.0/y,
    'abs': lambda x: abs(x[0]),
    'sum': lambda x: sum(x)
}

NARGS = {
    '+': 2,
    '-': 2,
    '*': 2,
    '/': 2,
    'abs': 1,
    'sum': 0,
}

def eval(s):
    if not s:
        return None
    st = []
    for tok in s.split(' '):
        tok = tok.lower()
        if tok.isdigit() or (tok[0] == '-' and tok[1:].isdigit()):
            st.append(int(tok))
        elif tok in OPS.keys() and len(st) >= NARGS[tok]:
            st, opargs = st[:-NARGS[tok]], tuple(st[-NARGS[tok]:])
            st.append(OPS[tok](opargs))
        else:
            return None
    return st[-1]



tests = [
    '4 5 +',
    '3 2 -',
    '4 5 + 3 -',
    '1',
    '',
    None,
    '4 +',
    '-3 abs', # 3 
    '4 5 + 3 sum' # 12
]


for t in tests:
    print eval(t)
