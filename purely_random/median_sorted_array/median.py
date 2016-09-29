# this is pseudocode!! not indented to work


def find_median(A, B):
    i = len(A) / 2
    k = (len(A) + len(B)) / 2    # this could be abstracted to find_k by receiving k as a param
    j = k - i - 2
    return search(A, B, i, j, k)


def search(A, B, i, j, k):
    if A[i] <= b[j+1] and B[j] <= A[i+1]:
            return max(A[i], B[j])
    elif A[i] > B[j+1]:
        return search(A, B, i/2, k - (i/2), k)
    elif B[j] > A[i+1]:
        return search(A, B, i + (len(A) - i)/2, k - (len(A) - i)/2, k)
