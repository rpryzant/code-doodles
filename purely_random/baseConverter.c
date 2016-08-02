/*
 * Reads in a number and two bases. Converts the number from the first base to the second.
 *    e.g. ./baseConverter 102 3 2         yeilds "1011" because it's 11 in base 3
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*
 * converts numbers to base 10
 */
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
 * finds the largest power of 'base' that fits in 'num'
 */
int largest_power_that_fits(int num, int base) {
    int d = 1;
    while (num / base > 0 || num == base) {
	num /= base;
	d += 1;
    }
    return d - 1;
}

/*
 * Converts numbers from base 10
 */
int from_base_10(int num, int to_base) {
    int acc = 0;
    int r = 0;
    int d = largest_power_that_fits(num, to_base);
    while (num > 0) {
	r = num / pow(to_base, d);
	acc += r * pow(10, d);
	num -= r * pow(to_base, d);
	d -= 1;
    }
    return acc;
}

int convert_via_base_10(int num, int from_base, int to_base) {
    num = to_base_10(num, from_base);
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
