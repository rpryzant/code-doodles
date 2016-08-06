def search_for_median(a, b):
    if not (a and b):
        return median(a) or median(b)
    median_index = (len(a) + len(b)) / 2
    return __search_for_median(a, 0, len(a)-1, b, median_index) or __search_for_median(b, 0, len(b)-1, a, median_index)

def median(a):
    mid = len(a) / 2
    if len(a) % 2 == 0:
        print mid
        return (a[mid-1] + a[mid] * 1.0) / 2
    else:
        return a[mid]

def __search_for_median(a, al, ah, b, ti):
    if al > ah:
        return None
    mid = (al + ah) / 2
    bi = get_index(a[mid], b)
    total_med = mid + bi
    if total_med == ti:
        if ti % 2 == 0:
            return (a[mid-1] + a[mid] * 1.0) / 2
        else:
            return a[mid]
    elif total_med > ti:
        return __search_for_median(a, al, mid-1, b, ti)
    else:
        return __search_for_median(a, mid+1, ah, b, ti)

def get_index(x, a):
    return __get_index(x, a, 0, len(a)-1)

def __get_index(x, a, l, h):
    if l > h:
        return l
    mid = (l + h) / 2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return __get_index(x, a, l, mid-1)
    else:
        return __get_index(x, a, mid+1, h)


test = [1,3,8,9]
print test
#print get_index(7, test, 0, len(test))

a = [1,2,7,9]
b = [3,4,8]
print a, b
print search_for_median(a, b)

a = [1]
b = [3,4]
print a, b
print search_for_median(a, b)

a = [2,5,6,8]
b = [1,3,9,11]
print a, b
print search_for_median(a, b)

a = [1,2]
b = [1,2]
print a, b
print search_for_median(a, b)

a = [1,2]
b = []
print a, b
print search_for_median(a,b)
