


# O(n log n) because each is `touched` once per node above it
# O(log n) space because recursive call acivation records
def isBalanced(root):
    if root is None:
        return True
    return abs(height(root.left) - height(root.right)) <= 1

def height(n):
    if n is None:
        return 0
    return max(height(n.left), height(n.right)) + 1


#O(n) time (memoized teh touching away)
# O(log n) space bc of recursive calls
def isBalanced2(root):
    cache = {}

    def height(n):
        if n is None:
            cache[id(n)] = 0
            return 0

        cache[id(n)] = max(height(n.left), height(n.right)) + 1
        return cache[id(n)]

    if root is None:
        return True
    return abs(height(root.left) - height(root.right)) <= 1



# roll functions to one
# reserve a "height" for unbalanced
# O(n) time (visit nodes once), O(log n) space (recursive calls)
def isBalanced(root):
    if root is None:
        return 0

    l = isBalanced(root.left)
    if l is None:
        return l
    
    r = isBalanced(root.right)
    if r is None:
        return r

    if abs(l - r) > 1:
        return None
    else:
        return max(l, r) + 1

def checkBalanced(root):
    return isBalanced(root) != None
