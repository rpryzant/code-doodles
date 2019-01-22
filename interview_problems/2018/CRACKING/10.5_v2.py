




def sparse_search(a, t):
    def find_nearest_nonblank(m, l, h):
        try:
            i = next( (i for i, x in enumerate(a[m:]) if x != '') ) 
        except StopIteration:
            try:
                i = -next( (i for i, x in enumerate(a[:m+1][::-1]) if x != '') ) 
            except StopIteration:
                return -1
        return m + i

    l = 0
    h = len(a)
    while l < h:
        m = (l + h) / 2
        if a[m] == '':
            m = find_nearest_nonblank(m, l, h)
            if m == -1: return None

        if a[m] == t:
            return m
        if a[m] < t:
            l = m + 1
        else:
            h = m - 1




test = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', 'zebra']
print sparse_search(test, 'ball')
print sparse_search(test, 'dad')
print sparse_search(test, 'zebra')
