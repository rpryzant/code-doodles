import re

def urlify_smartest(s):
    return s.replace(' ', '%20')

def urlify_semismart(s):
    parts = re.findall('[^ ]', s)
    return '%20'.join(p for p in parts)

def urlify_dumb(arr):
    i = 0
    l = len(arr)
    while i < l:
        if arr[i] == ' ':
            arr = insert(arr, i)
            i += 2
            l += 2
        i += 1
    return arr


def insert(arr, i):
    arr[i] = "%"
    arr.insert(i+1, '2')
    arr.insert(i+2, '0')
    return arr

print urlify_dumb(['h','e',' ',' ','w','a',' '])
