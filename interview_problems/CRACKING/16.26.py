# i like my solution to this one! 
# a varient of this would be a great question to ask others


import re


def calculate(expression):
    NEXT = {'\+|\-': '\*|\/', '\*|\/': ''}
    OPS = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x * 1.0 / y}

    def solve(exp, splitter):
        subexps = re.split(splitter, exp)
        expops = re.findall(splitter, exp)
        if len(subexps) == 1 and subexps[0].isdigit():
            return int(subexps[0])
        subexps = map(lambda x: solve(x, NEXT[splitter]), subexps)
        for i in range(len(expops)):
            subexps[i+1] = OPS[expops[i]](subexps[i], subexps[i+1])
        return subexps[-1]
    return solve(expression, '\+|\-')

print calculate('2*3+5/6+3+15')
