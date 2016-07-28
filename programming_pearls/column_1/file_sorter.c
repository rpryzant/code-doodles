/* This program sorts data from stdin
 *   e.g. ./fileSorter < sample.txt
 */

#include <stdio.h>

int intcomp(int *x, int *y) {
    return *x - *y;
}

int a[1000000];

int main(void) {
    int i, n = 0;
    while (scanf("%d", &a[n]) != EOF) {
	n++;
    }
    qsort(a, n, sizeof(int), intcomp);
    for (i = 0; i < n; i++)
	printf("%d\n", a[i]);
    return 0;
}
