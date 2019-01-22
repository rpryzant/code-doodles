# I like this better!!


def pascal(n):
    assert n > 0, 'n must be positive'

    out = [[1]]
    for _ in range(n-1):
        prev = [0] + out[-1] + [0]
        out.append([sum(prev[i:i+2]) for i in range(len(prev) - 1)])

    return out

print pascal(1)
print pascal(5)
