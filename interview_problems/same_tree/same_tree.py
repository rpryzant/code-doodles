


def equals(a, b):
    return a != None and b != None and a.data == b.data


def same_tree(a, b):
    if not a and not b:
        return True

    if not equals(a, b):
        return False

    return same_tree(a.left, b.left) and same_tree(a.right, b.right)
