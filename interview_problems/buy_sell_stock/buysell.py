"""
p1 p2 ... pn

want to pick pa, pb : (pb - pa) = MAX{pj - pi} for i in [1, n], j in (i, n]

aka bggest difference between elements of the array, ordering imposed


lets consider some pk
   pretend its the price we want to *sell* at
   then the matching buy point is going to be argmin(p1 ... pk-1)

   lets say its the price we want to *buy* at
   then the matching sell point is argmax(pk+1 ... pn)


1) brute force
    consider all pi as buy point
    evaluate argmax of rest of array
    get diff, save max diff



2) O(n)
     get buy point from argmin, sell from corresponding argmax
     problem: [2, 19, 1]
     
     get pi = argmin, pj = argmax
        test pk = argmax(i .. n) with pi
        test pl = argmin(1 ... j) with pj
        take best of two 
     guarenteed to get optimal answer because ONE endpoint is going to be a max/min

3) 1 pass
     track min so far
     compare with current element
     if < min, set min
     else get diff
     if diff > cur, set the two 



"""

def argmax(arr):
    return max((x, i) for i, x in enumerate(arr))



def best_time_bf(A):
    m = [None, None, None]
    for i, buy in enumerate(A[:-1]):
        sell = argmax(A[i+1:])
        if not m[2] or sell[0] - buy > m[2]:
            m = [i, sell[1], sell[0] - buy]
    return m[2] if m[2] > 0 else 0


print best_time_bf([7, 1, 5, 3, 6, 4])






def best_time_better(arr):
    out = [None, None, None]

    for i, x in enumerate(arr):
        if not out[0] or out[0] > x:
            out[0] = i
        elif not out[1] or x - arr[out[0]] > out[2]:
            out[1] = i
            out[2] = x - arr[out[0]]

    return out[2] or 0


print best_time_better([7, 1, 5, 3, 6, 4])
