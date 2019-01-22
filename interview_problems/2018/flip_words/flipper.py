



def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def reverse_chunk(arr, i, j):
   if i == j or i > j:
       return
   swap(arr, i, j)
   reverse_chunk(arr, i+1, j-1)

def next_j(arr, i):
   while i < len(arr) - 1 and arr[i + 1] != ' ':
      i += 1
   return i

def reverse(arr):
   arr = arr[::-1]
   i = 0
   j = next((i for i, c in enumerate(arr) if (i+1 == len(arr)) or (arr[i+1] == " ")))
   while i < len(arr):
      tmpi = i
      tmpj = j
      reverse_chunk(arr, tmpi, tmpj)
      i = j + 2
      j = next_j(arr, i)
   return arr


test = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

print test
print reverse(test)
