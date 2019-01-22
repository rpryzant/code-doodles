""" 
STACKS ARE GREAT FOR ALL THINGS PARENS!!
"""



def count_brackets(s):
    assert all(x in ['(', ')'] for x in s)
    out = 0
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) == 0:
                out += 1
            else:
                stack.pop()
    return out + len(stack)


print count_brackets("())(")
print count_brackets("()(")
print count_brackets("())")
print count_brackets("(()")
print count_brackets("())")
print count_brackets("()(())")
