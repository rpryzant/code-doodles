


def list_depths(head):
    lists = []
    def dfs(n, depth):
        if n == None:
            return
        if len(lists) < depth:
            lists += [None for _ in range(depth - len(lists))]
        if lists[depth - 1] is None:
            lists[depth - 1] = Node(n.data)
        else:
            lists[depth - 1] = Node(n.data)
        dfs(n.left, depth + 1)
        dfs(n.right, depth + 1)


    dfs(head, 1)
    return depths
