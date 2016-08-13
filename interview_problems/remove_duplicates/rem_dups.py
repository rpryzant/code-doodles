

def remove_dups(a):
    repeats = 0
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            repeats += 1
        else:
            a[i-repeats] = a[i]
    return len(a) - repeats


test = [1,2,2,2,2,3,4,5,5,6,7]
print remove_dups(test), test

test = [1,1,2]
print remove_dups(test), test
