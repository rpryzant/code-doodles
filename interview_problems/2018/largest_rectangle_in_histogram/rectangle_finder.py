# i like my solution to this one!

def find_largest_rectangle(h):
    s = []
    m = -1
    for i in range(len(h)):
        collapse(s)
        if s and s[-1][1] > m:
            m = s[-1][1]
        s.append([h[i], h[i]])
    collapse(s)
    return m if s[-1][1] < m else s[-1][1]

def collapse(s):
    if len(s) < 2:
        return
    if s[-1][0] <= s[-2][0] and s[-1][1] + s[-1][0] >= s[-2][1]:
        tmp = s.pop()
        s.pop()
        s.append([tmp[0], tmp[1] + tmp[0]])
    elif s[-2][0] <= s[-1][0] and s[-2][1] + s[-2][0] >= s[-1][1]:
        s.pop()
        s[-1][1] += s[-1][0]



print find_largest_rectangle([2,1,5,6,2,3])


