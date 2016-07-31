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

* If memory constraints were tighter than 1.25mb, I'd sort in multiple passes. Start by reading the first `N/2` digits into memory, sorting, and writing.
Since these are the smaller numbers, you don't need to mess with the `fp` and can continue writing where you left off
when you read the 2nd half of the data into memory. With less memory, break into quarters or whatever. 
Note that a `k` pass algorithm can sort at most `N/k` elements at a time, takes up `N/k * 4` bytes of memory, and takes `Nk` time. 

* **first idea:** if each int could appear at most 10 times (instead of just once) my first thought is to store multiple vectors. if a flag is already set in
one vector then i'd just set the flag in the next vector. this means that i'd have to drastically increase the number of passes (tenfold!). 
**better idea**: instead of a *bit*vector, we can use a *nibble*vector (each entry is 4 bits). each nibble can track the number of occurances up to 2^4 = 16 for the associated num

* Again a nibble vector. The first bit's index corresponds to the lower 7 digits of the phone number. The second two bits are reserved for differentiating between each area code. Sort the same way as before: read the file into the bit vector and then write back to a new file by scanning through the vector. 

* Technique for initializing elements of an array to 0 the first time they're accessed (lazy initialization).
  * **first idea**. initialize a bitvector that mirrors the input (1 bit per array elem) and keeps a record of fresh accesses. When accessing array element `i`, check the `i`th bit in the vector. If it's 0, set the array to 0 and flip the bit in the vector. Otherwise, don't init. `O(n)` space and `O(1)` time .
  * **second idea** hmm...can I bring it down on space? Looks like not! The book's solution is `O(32 * 2n)` because they init 2 n-element integer arrays!

* Hash table...duhhhh. Hash into a small number of buckets though so that workers can retrieve letters quickly.

* 

* going to sleep...*TODO*: 8, 9, 10, 11, 12

*