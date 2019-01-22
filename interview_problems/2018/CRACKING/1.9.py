

def is_rotation(a, b):
    if a is not "" and len(a) == len(b):
        return isSubstring(a+a, b)
