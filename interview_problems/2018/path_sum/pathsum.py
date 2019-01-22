


def is_sum(root, n):
    def dfs(node, cur, target):
        if not node:
            return True if target == cur else False
        return dfs(n.left, cur + n.left.data, target) or \
               dfs(n.right, cur + n.right.data, target)

    return dfs(root, root.data, n)
