
def swap_in_place(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

