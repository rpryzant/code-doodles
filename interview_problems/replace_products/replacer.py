

def replace_products(A):
    l = [[1, 1] for _ in range(len(A))]
    i = 1
    j = len(l) - 2

    while i < len(l):
        l[i][0] = l[i-1][0] * A[i-1]
        l[j][1] = l[j+1][1] * A[j+1]
        i += 1
        j -= 1

    return [x[0] * x[1] for x in l]


print replace_products([1,2,3,4])
