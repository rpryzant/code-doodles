#include <stdio.h>
#include <limits.h>

/* 
 * Implementation of radix sort
 */


int get_max(int a[], int size) {
    int max = INT_MIN;
    for (int i = 0; i < size; i++) {
	if (a[i] > max)
	    max = a[i];
    }
    return max;
}

int digit_at_significance(int x, int sig) {
    return (x / sig) % 10;
}

void print(int a[], int size) {
    for (int i = 0; i < size; i++) {
	printf("%d ", a[i]);
    }
    printf("\n");
}

void sort(int a[], int size) {
    int i;
    int tmp[size];
    int max = get_max(a, size);
    int sig = 1; // base 10

    // sort a via repeated sortings at successive significance levels
    while (max / sig > 0) {
	int buckets[10] = {0};
	// get frequency of each digit in the sig's place (e.g. 10's place)
	for (i = 0; i < size; i++)
	    buckets[digit_at_significance(a[i], sig)]++;
	// cdf of frequency buckets
	//    buckets[i] now points to where the last element of a[] 
	//    with i in the sig's place will be in tmp[]
	//
	//    e.g. if buckets[2] = 3 and sig = 10, than the last number in tmp[]
	//       with a 2 in the 10's place will be at index 3
	for (i = 1; i < 10; i++) 
	    buckets[i] += buckets[i - 1];
	// place element's of a[] into their sorted order
	for (i = size - 1; i >= 0; i--) {
	    // -1 because buckets is 1-indexed at this point, not 0-indexed
	    tmp[buckets[digit_at_significance(a[i], sig)] - 1] = a[i]; 
	    buckets[digit_at_significance(a[i], sig)]--;
	}
	// update a[] with tmp[] and move to the next significance level
	for (i = 0; i < size; i++)
	    a[i] = tmp[i];
	sig *= 10;
    }
}

int main() {
    int arr[] = {170, 45, 75, 90, 802, 24, 2, 66};
    int size = sizeof(arr) / sizeof(arr[0]);
    print(arr, size);
    sort(arr, size);
    print(arr, size);
}
