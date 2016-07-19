import java.util.Arrays;

public class MinHeap {
    
    private int[] A;
    private int size;
    

    public MinHeap() {
	this.A = new int[100];
	this.size = 0;
    }

    public int getSize() {
	return this.size;
    }

    public void insert(int x) {
	if (size == A.length - 1) 
	    doubleSize();
	
	A[size] = x;
	int i = size;
	size++;
	int tmp;
	while (i >= 0 && A[i] < A[parent(i)]) {
	    System.out.println(i + "|"+ A[i] + " " + parent(i) + "|" +A[parent(i)]);
	    tmp = A[parent(i)];
	    A[parent(i)] = A[i];
	    A[i] = tmp;
	    i = parent(i);
	}
    }

    public int peek() {
	return A[0];
    }

    public int pop() {
	int result = A[0];
	
	int i = 0;
	while (i < size) {
	    if (A[leftChild(i)] < A[rightChild(i)]) {
		A[i] = A[leftChild(i)];
		i = leftChild(i);
	    } else {
		A[i] = A[rightChild(i)];
		i = rightChild(i);
	    }
	}
	return result;
    }

    private int leftChild(int i) {
	return 2 * i + 1;
    }

    private int rightChild(int i) {
	return 2 * i + 2;
    }

    private int parent(int i) {
	return (i - 1) / 2;
    }

    private void doubleSize() {
	int[] n = new int[A.length * 2];
	for (int i = 0; i < A.length; i++)
	    n[i] = A[i];
	A = n;
    }

    public void print() {
	System.out.println(Arrays.toString(A));
    }

    public static void main(String[] args) {
	MinHeap h = new MinHeap();
	h.insert(1);
	h.insert(3);
	h.insert(6);
	h.insert(5);
	h.insert(9);
	h.insert(8);
	h.print();
	h.insert(-2);
	h.print();
	h.pop();
	h.print();
    }
}