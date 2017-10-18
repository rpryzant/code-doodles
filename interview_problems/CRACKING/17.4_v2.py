"""
is A sorted?     ===> NO

a = [0, 1, 2, …, n] but is missing some 0 <= k <= n
ex:
a = [3, 2, 4, 0]   (missing 1)


if no constraints: 
    throw into dict, then iterate through
    use bit vector to track elems, find first 0
    sum(1 through n) - sum(A) = missing
breakages:
can only access one bit at a time
O(n)


a = [3, 2, 4, 0]   (missing 1)
011
010
100
000

maybe predict the expected count of each bit, calculate true O(32 * n), and recover missing? NO, UNLIKELY


a = [0, 2, 3]
00
10
11

hard to plan access because i don’ot know the ordering!!

0 1 2 3 4 5
0 1 1 2 2 3
0 1 0 1 0 1

bit 0
expected 1’s: n+1 / 2
if missing is odd:
    too few 1’s
if missing is even:
    too many 1’s
0  1  2  3  4  5
0  0  1  2  2  2  3  4 4  4
00 01 10 11 0  0
bit 1:
expexted 1’s: 
((n / 4) * 2) + ((n % 4) - 1)
num chunks        how many from last partial chunk


bit 2
((n / 8) * 4) + ((n % 8) - 3)
000
001
010
011
100

bit i
chunk_size = 2^{i+1}
1s_in_chunk = 2^i
(n / chunk_size) * 1s_in_chunk + ((n % chunk_size) - (1s_in_chunk-1))
"""

def expected_bits(i, n):
    chunk_size = float(2 ** (i+1))
    1s_in_chunk = 2**i
    return (n / chunk_size) * 1s_in_chunk + \
           ((n % chunk_size) - (1s_in_chunk - 1))

def get_bit(x, i):
    return (x & 1 << i) >> i

def set_bit(x, i):
    return x |= (1 << i)

def find_missing_num(a, n):
    out = 0
    for bit in range(32):
        expected_1s = expected_bits(bit, n)
        observed_1s = sum(get_bit(x, i) for x in a)
        if observed < expected or \
                (observed == expected and get_bit(a[0], bit)):
            set_bit(out, bit)
    return out

