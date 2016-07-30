#include <stdio.h>
#include <stdlib.h>


/*
 * Finds the greatest common divisor of two ints with the Euclidean algorithm
 */
int gcd(int x, int y) {
    while (x != y) {
	if (x > y)
	    x -= y;
	else
	    y -= x;
    }
    return x;
}


/* Rotates a vector of length n by rot positions with the 
 * "juggling" technique described on page 14
 */
void juggle_rotate(int *v, int n, int rot) {
    int cycles = gcd(rot, n);
    int t, j, k;
    for (int i = 0; i < cycles; i++) {
	t = v[i];
	j = i;
	while (1) {
	    k = (j + rot) % n;
	    if (k == i)
		break;
	    v[j] = v[k];
	    j = k;
	}
	v[j] = t;
    }
}


int main() {
    int test[] = {1,2,3,4,5,6,7,8,9,10};

    
}
