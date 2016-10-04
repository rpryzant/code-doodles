


def num_trees(n):
    cache = {}
    def nt(n):
        if cache.get(n):
            return cache[n]
        elif n < 1:
            set = 0
        elif n == 1:
            set = 1
        else:
            set = 2 * nt(n - 1) + nt(n - 2) ** 2
        cache[n] = set
        return cache[n]

    return nt(n)

# bst is the same! Same structural constraints on topology - you can cook up
#    the right numbers to make any binary tree topology a valid bst topology



print num_trees(1)
print num_trees(2)
print num_trees(3)
print num_trees(4)
print num_trees(20)
