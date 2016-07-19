import java.util.Arrays;
import java.lang.Comparable;
import java.lang.StringBuilder;

public abstract class Heap <T extends Comparable<T>>{

    protected T[] A;
    protected int size;

    public Heap() {
	this.A = (T[])new Comparable[100];
	this.size = 0;
    }

    abstract public void insert(T x);

    abstract public T pop();

    public int getSize() {
	return size;
    }

    public T peek() {
	return (T)A[0];
    }

    protected int leftChild(int i) {
	return 2 * i + 1;
    }

    protected int rightChild(int i) {
	return 2 * i + 2;
    }

    protected int parent(int i) {
	return (i - 1) / 2;
    }

    protected void doubleSize() {
	T[] n = (T[])new Comparable[A.length * 2];
	for (int i = 0; i < A.length; i++)
	    n[i] = A[i];
	A = n;
    }

    public void print() {
	StringBuilder s = new StringBuilder();
	for (int i = 0; i < size; i++)
	    s.append(A[i] + " ");
	System.out.println(s.toString());
    }
}