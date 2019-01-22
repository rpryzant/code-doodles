import math


def get_primes(max):
    candidates = [True for _ in range(max)]
    candidates[0] = False

    for i , flag in enumerate(candidates):
        if not flag:
            continue
        for j in (index + i for index, f in enumerate(candidates[i+1:]) if f):
            if (j+1) % (i+1) == 0:
                candidates[j] = False

    return [i+1 for i, x in enumerate(candidates) if x]







def is_prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True



print get_primes(100)
