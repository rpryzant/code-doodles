

# swaps two array elements in place
def swap(a, i, j):
    a[i] = a[i] + a[j]
    a[j] = a[i] - a[j]
    a[i] = a[i] - a[j]

def sort(a):
    for _ in range(len(a)):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                swap(a, i, i + 1)

test = [6,3,2,-5,9]
sort(test)
print test
