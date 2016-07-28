Solutions to problems below

* see `file_sorter.c` for a file sorter which uses a library (in this case `qsort` from the standard library)
* see `bitvector_sorter.c` for a file sorter which uses a bit vector like the one discussed in this column
* same as #2
* pseudocode:
```
for i in [0, n)
    x[i] = i
for i in [0, k)
    swap(i, randint(i, n-1))
```
this fills up an array and then mixes it up with some well placed swaps

* I'd sort in multiple passes. Start by reading the first `N/2` digits into memory, sorting, and writing.
Since these are the smaller numbers, you don't need to mess with the `fp` and can continue writing where you left off
when you read the 2nd half of the data into memory. With less memory, break into quarters or whatever. 
Note that a `k` pass algorithm can sort at most `N/k` elements at a time, takes up `N/k * 4` bytes of memory, and takes `Nk` time. 

* dfs