import java.lang.*;
import java.util.*;

public class QuickSort <T extends Comparable<T>>{

    public static void main(String[] args) {
	QuickSort sorter = new QuickSort();

	Integer[] test = {0, 23, -4, 4, 5};
	sorter.sort(test);
	System.out.println(Arrays.toString(test));
    }

    public QuickSort() {
    }

    public void sort(T[] a) {
	sortR(a, 0, a.length - 1);
    }

    private void sortR(T[] a, int low, int high) {
	if (low >= high) 
	    return;
	int p = partition(a, low, high);
	sortR(a, low, p - 1);
	sortR(a, p + 1, high);
    } 

    private int partition(T[] a, int low, int high) {
	T pivot = a[high];

	int i = low;
	for (int j = low; j < high; j++) {
	    if (a[j].compareTo(pivot) < 0) {
		swap(a, i, j);
		i++;
	    }
	}
	swap(a, i, high);
	return i;
    }

    private void swap(T[] a, int i, int j) {
	T tmp = a[i];
	a[i] = a[j];
	a[j] = tmp;
    }

}