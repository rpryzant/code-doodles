# -*- coding: utf-8 -*-
"""
[ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
[ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't' ]



1: brute force
convert to words
reverse
convert to chars

return [c for c in ‘’.join(arr).split(‘ ‘)[::-1]]
O(n)
O(n) space (# of chars)

2: improve space
loop through chars, maintain list of (word_start, word_end)
reverse that list of tuples, then construct outgoint and return

O(n) / O(n)  (because not in place)


3: in place
[w1  w2 .. wk][::-1] = [wk, .., w2 w1]
pointers to front, back and reverse each in-place
seems prohibitively messy to implement
(what if word runs over? etc etc)

4: better in-place
arr = [w1 w2 .. wn]
arr[::-1] = [wnR .. w2R w1R]
then reverse each word in arr

O(n) time, O(1) space
"""
def swap(a, p, q):
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp

def reverse(a, i, j):
    # reverses i to j in a
    if i == j or i > j: return
    swap(a, i, j)
    reverse(a, i+1, j-1)

def word_boundary(seq, i):
    try:
        return next((
                x+i+1 for x, ch in enumerate(seq[i+1:]) if ch == ' '))
    except StopIteration:
        return len(seq)

def flip(seq):
    reverse(seq, 0, len(seq)-1)
    i = 0
    while i < len(seq):
        j = word_boundary(seq, i)
        reverse(seq, i, j - 1)
        i = j + 1

test = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

print test
flip(test)
print test
