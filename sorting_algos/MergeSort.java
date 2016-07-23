import java.util.*;
import java.lang.*;



public class MergeSort <T extends Comparable<T>> {


    public MergeSort() {
    }

    public T[] sort(T[] a) {
	return sortR(a, 0, a.length - 1);
    }    

    private T[] sortR(T[] a, int low, int high) {
	if (low >= high) {
	    return a;
	}
	int mid = (low + high) / 2;
	sortR(a, low, mid);
	sortR(a, mid + 1, high);
	return merge(a, low, mid, high);
    }

    private T[] merge(T[] a, int low, int mid, int high) {
	T[] copy = Arrays.copyOf(a, a.length);
	int outi = low;
	int ai = low;
	int bi = mid + 1;
	while (ai <= mid && bi <= high) {
	    if (copy[ai].compareTo(copy[bi]) < 0) {
		a[outi] = copy[ai];
		ai++;
	    } else {
		a[outi] = copy[bi];
		bi++;
	    }
	    outi++;
	}
	while (ai <= mid) {
	    a[outi] = copy[ai];
	    ai++;
	    outi++;
	}
	return a;
    }

    public static void main(String[] args) {
	MergeSort sorter = new MergeSort();

	Integer[] test = {3,6,2,8,2,3,1};
	System.out.println(Arrays.toString(test));
	System.out.println(Arrays.toString(sorter.sort(test)));

	Integer[] test2 = {3,6,2,-8,2,-3,1};
	System.out.println(Arrays.toString(test2));
	System.out.println(Arrays.toString(sorter.sort(test2)));

	Integer[] test3 = {1,2,2,3,3,6,8};
	System.out.println(Arrays.toString(test3));
	System.out.println(Arrays.toString(sorter.sort(test3)));
    }
}