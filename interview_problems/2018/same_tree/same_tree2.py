"""
there’s gotta be some kind of recurrence

EXAMPLES
1 check for root equality, then check nodes
   a 

2 make sure left & right are equal, then check roots
     a 
left   right


joint dfs, ensuring node equality along the way

n1, n2

l_valid = check(n1.left, n2.left)
r_valid = check(n1.right, n2.right)

if l_valid and r_valid and n1.data == n2.data:
    return True
else:
return False

"""



def check(n1, n2):
    # handle corner cases
    assert isinstance(n1, (NoneType, Node)) and \
           isinstance(n2, (NoneType, Node))

    # base case
    if all(map(lambda x: x is None, [n1, n2])):
        return True
    elif any(map(lambda x: x is None, [n1, n2])):
        return False

    # recurse
    valid_left = check(n1.left, n2.left)
    valid_right = check(n1.right, n2.right)

    return valid_left and valid_right and n1.data == n2.data



def check_better(n1, n2):
    # handle corner cases
    assert isinstance(n1, (NoneType, Node)) and \
           isinstance(n2, (NoneType, Node))

    # base cases
    if n1 is None and n2 is None:
        return True
    if not (n1 != None and n2 != None and n1.data == n2.data):
        return False

    # recurse
    valid_left = check(n1.left, n2.left)
    valid_right = check(n1.right, n2.right)

    return valid_left and valid_right


