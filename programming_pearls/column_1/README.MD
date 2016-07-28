Solutions to problems below

1. see `file_sorter.c` for a file sorter which uses a library (in this case `qsort` from the standard library)
2. see `bitvector_sorter.c` for a file sorter which uses a bit vector like the one discussed in this column
3. same as #2
4. pseudocode:
```
for i in [0, n)
    x[i] = i
for i in [0, k)
    swap(i, randint(i, n-1))
```
this fills up an array and then mixes it up with some well placed swaps
5. 