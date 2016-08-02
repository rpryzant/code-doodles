/*
 * Reads in a number and two bases. Converts the number from the first base to the second.
 *    e.g. ./baseConverter 102 3 2         yeilds "1011" because it's 11 in base 3
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int to_base_10(int num, int from_base) {
    int acc = 0;
    int multiplyer = 1;
    while (num > 0) {
	acc += ((num % 10) % from_base) * multiplyer;
	multiplyer *= from_base;
	num /= 10;
    }
    return acc;
}

/*
 * TODO FINISH - THIS GREEDY METHOD DOESN'T WORK 
 */
int from_base_10(int num, int to_base) {
    int acc = 0;
    int r = 0;
    int d = 0;
    while (num > 0) {
	r = num % to_base;
	if (r > 0) {
	    acc += r * pow(10, d);
	    num -= r * pow(to_base, d);
	} else if (num == to_base) {
	    acc += 1 * pow(10, d);
	} else {
	    num /= to_base;
	}
	d++;
    }
    return acc;
}


int convert_via_base_10(int num, int from_base, int to_base) {
    num = to_base_10(num, from_base);
    printf("%d\n", num);
    return from_base_10(num, to_base);
}



int main(int argc, char *argv[]) {
    if (argc < 4) {
	printf("Usage: number [base to] [base from]\n");
	return -1;
    }

    int num = atoi(argv[1]);
    int i = atoi(argv[2]);
    int j = atoi(argv[3]);

    num = convert_via_base_10(num, i, j);
    printf("%d\n", num);
}
