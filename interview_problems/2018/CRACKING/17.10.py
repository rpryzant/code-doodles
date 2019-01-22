# its not what she gave in the book, but i like my solution! I got it working on the first try!


# O(n^2) time O(1) space
def find_majority_brute(a):
    for x in a:
        if validate(a, x):
            return x
    return -1

def validate(a, x):
    return sum(1 if y == x else 0 for y in a) > (len(a) / 2)


# O(n log n) time O(1) space
def find_majority_better(a):
    a = sorted(a)
    i = 0
    l = len(a)
    while i < l - 1:
        j = end_range(a, i)
        if j - i >= l / 2:
            return a[i]
        i = j
    return -1

def end_range(a, i):
    return next( (i + j + 1 for j, y in enumerate(a[i+1:]) if y != a[i]) )


test = [1,2,5,9,5,9,5,5,5]

print find_majority_brute(test)
print find_majority_better(test)
        

test = [1,2,3,9,5,9,5,10,5]


print find_majority_brute(test)
print find_majority_better(test)
