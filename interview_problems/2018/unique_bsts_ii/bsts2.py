


def bsts(n):
    assert n > 0

    def recurse(arr):
        out = []
        if len(arr) == 0:
            return [None]

        for i, x in enumerate(arr):
            for left_subtree in recurse(arr[:i]):
                for right_subtree in recurse(arr[i+1:]):
                    root = Node(x)
                    root.left = left_subtree
                    root.right = right_subtree
                    out.append(root)
        return out


    return recurse(range(1, n+1))
