



def is_valid(n):
    if n is None:
        return False

    valid_left = True if n.left is None or (n.left.d < n.d and is_valid(n.left)) else False
    valid_right = True if n.left is None or (n.left.d < n.d and is_valid(n.left)) else False

    return valid_left and valid_right

