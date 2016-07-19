import java.util.Arrays;
import java.lang.*;

public class MaxHeap<T extends Comparable<T>> extends Heap<T> {

    public MaxHeap() {
	super();
    }

    public void insert(T x) {
	if (size == A.length - 1) 
	    doubleSize();
	A[size] = x;
	int i = size;
	size++;
	T tmp;
	while (A[i].compareTo(A[parent(i)]) > 0) {
	    tmp = (T)A[parent(i)];
	    A[parent(i)] = A[i];
	    A[i] = tmp;
	    i = parent(i);
	}
    }

    public T pop() {
	int i = 0;
	T result = (T)peek();
	int childIndex = i;

	while (leftChild(i) < size || rightChild(i) < size) {
	    if (leftChild(i) < size)
		childIndex = leftChild(i);
	    if (rightChild(i) < size && A[rightChild(i)].compareTo(A[childIndex]) > 0)
		childIndex = rightChild(i);	    
	    A[i] = A[childIndex];
	    i = childIndex;
	}
	A[i] = null;
	size--;
	return result;
    }
