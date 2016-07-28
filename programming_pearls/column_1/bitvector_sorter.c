
#include <stdio.h>

int VECTOR_SIZE = 100;

/*
 * adds or removes element from set
 */
void set_flag(int *a, int x, int set) {
    int b = x / sizeof(int);
    int i = x % sizeof(int);
    if (set)
	a[b] |= (1 << i);
    else
	a[b] &= ~(1 << i);
}

/*
 * finds and pops smallest element in set
 */
int pop_flag(int *a) {
    int n, i = 0;
    for (int b = 0; b < VECTOR_SIZE; b++) {
	i = a[b];
	for (int k = 0; k < sizeof(int) * sizeof(char); k++) {
	    if (i & 1) {
		n = k + b * (sizeof(int) * sizeof(char));
		set_flag(a, n, 0);
		return n;
	    }
	    else {
		i >>= 1;
	    }
	}
    }
    return -1;
}

int main() {
    int a[100] = { 0 };
    int tmp, n = 0;
    while (scanf("%d", &tmp) != EOF) {
	set_flag(a, tmp, 1);
	n++;
    }
    while (n) {
	printf("%d\n", pop_flag(a));
	n--;
    }
    return 0;
}
