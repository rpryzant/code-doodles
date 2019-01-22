
# I prefer this!


def rmNode(root, n):
    if n < 0; return root

    L = 0
    runner = root
    while runner != None:
        runner = runner.next
        L += 1

    if L - n < -1: return root
    if L - n == -1: return root.next

    runner = root
    for _ in range(L - n):
        runner = runner.next
    runner.next = runner.next.next
    
    return root
