
def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def sort(a):
    return sortR(a, 0, len(a) - 1)

def partition(a, low, high):
    pivot = a[high]

    i = low
    for j in range(low, high):
        if a[j] <= pivot:
            swap(a, i, j)
            i += 1
    swap(a, i, high)
    return i

def sortR(a, low, high):
    if low >= high:
        return a

    pivot_index = partition(a, low, high)
    sortR(a, low, pivot_index - 1)
    sortR(a, pivot_index + 1, high)



test = [1,6,-2, 4]
sort(test)
print test

    
