from random import random
from collections import defaultdict

def rand5():
	return int(random() * 5)
	
	
def rand7():
	while True:
		x = ( rand5() * 5 ) + rand5() 
		if x < 21:
			return x % 7


d = defaultdict(lambda: 0)
for i in range(10000):
    d[rand7()] += 1

print d
