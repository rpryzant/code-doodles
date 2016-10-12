

def min_sum(T):
    if not T:
        return 0
    min = [None]

    def ms(level, i, sofar):
        if level == len(T):
            if min[0] == None or sofar < min[0]:
                min[0] = sofar
            return

        ms(level + 1, i, sofar + (T[level + 1][i] if level < len(T)-1 else 0))
        ms(level + 1, i + 1, sofar + (T[level + 1][i+1] if level < len(T)-1 else 0))
        return

    ms(0, 0, T[0][0])
    return min[0]



test = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print min_sum(test)
