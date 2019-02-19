"""number of paths 


start (0, 0)
end   (n-1, n-1)

cant cross diagonal if (x, y), need x <= y

can move diagonally? no
wrap around edge like pac man? no
can only go N or E


O(n ^2) 
"""
def npaths(n):
    assert n > 0

    cache = {}
    def recurse(x, y):
        if (x, y) in cache:
            return cache[x, y]

        if x > y or x >= n or y >= n:
            return 0
        elif x == n - 1 and y == n - 1:
            return 1

    cache[(x, y)] = recurse(x + 1, y) + recurse(x, y + 1)
    return cache[x, y]

return recurse(0, 0)






