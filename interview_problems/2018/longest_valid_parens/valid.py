

def longest_valid(s):
    l = 0
    mx = 0
    stack = []
    for c in s:
        if c == '(':
            stack.append("*")
            l += 1
        else:
            if len(stack) > 0:
                stack.pop()
                l += 1
            else:
                l = 0
            if l > mx:
                mx = l

    return mx
        
print longest_valid("(")
print longest_valid(")()")
print longest_valid(")()())")
print longest_valid("(()(()")
