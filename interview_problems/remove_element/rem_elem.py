

def remove_occurances(a, t):
    n = 0
    for i in range(len(a)):
        if a[i] == t:
            n += 1
        else:
            a[i-n] = a[i]
    return len(a) - n


test= [3,2,2,3]
print remove_occurances(test,3), test

