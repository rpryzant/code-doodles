"""converstoin

count number of bits to flip a into b



are a + b both ints? ⇒ yes


11011   1 2 8 16 27
01111   1 2 4 8  15
^ ^
10100

xor
count 1’s


"""



def count_swap(x, y):
	xor = x ^ y
	out = 0
	while xor > 0:
		out += (xor & 1)
		xor >>= 1
	return out




