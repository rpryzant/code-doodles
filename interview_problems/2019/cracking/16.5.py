"""factorial zeros

number of trailing zeros in n factorial

n is positive? 
int?

are we given n factorial? or n? 

bigger than 100? smaller than 100? 

where do zeros come from?
	 10s!

	5 2
	10

6 5 4 3 2 1
	5 2 -> 10

9 8 7 6 5 4 3 2 1
	5 2 -> 10

10 9 8 7 6 5 4 3 2 1
	10
	5 2
	2 0s

15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
    180        10            10

if smaller than 100: """


def num_zeros(n):
	tens = n / 10
	fives_twos = sum([
		1 if x % 10 in [5, 2] else 0 for x in range(n+1)
	]) // 2
	return tens + fives_twos

print num_zeros(15)
print num_zeros(14)


