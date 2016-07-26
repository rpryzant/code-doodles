import java.lang.*;
import java.util.*;

// scope restricted to this package
class Node {
    public int data;
    public Node left;
    public Node right;

    public Node(int data) {
	this.data = data;
	this.left = null;
	this.right = null;
    }

    public boolean hasNoChildren() {
	return (this.left == null && this.right == null);
    }
}

public class BinarySearchTree {
    public Node root;

    public BinarySearchTree() {
	this.root = null;
    }

    public BinarySearchTree(Node root) {
	this.root = root;
    }

    public void insert(int d) {
	if (root == null) {
	    root = new Node(d);
	} else {
	    insertR(root, d);
	}
    }

    private void insertR(Node n, int d) {
	if (d < n.data) {
	    if (n.left == null) {
		n.left = new Node(d);
	    } else {
		insertR(n.left, d);
	    }
	} else {
	    if (n.right == null) {
		n.right = new Node(d);
	    } else {
		insertR(n.right, d);
	    }
	}
    }

    public void delete(int d) {
	deleteR(root, d);
    }

    private void deleteR(Node n, int d) {
	if (n == null) {
	    return;
	} else if (n.data == d) {
	    if (n.hasNoChildren()) {
		n = null;
		return;
	    } else {
		int min = getMin(n.right);
		n.data = min;
	    }
	} else if (n.data > d) {
	    deleteR(n.right, d);
	} else {
	    deleteR(n.left, d);
	}
    }

    private int getMin(Node n) {
	if (n == null) {
	    return -1;
	} else if (n.left == null) {
	    int x = n.data;
	    n = n.right;
	    return x;
	} else {
	    return getMin(n.left);
	}
    }

    public void printPretty() {
	printPretty(root, "");
    }

    private void printPretty(Node n, String s) {
	if (n != null) {
	    printPretty(n.right, '\t' + s);
	    System.out.println(s + n.data);
	    printPretty(n.left, '\t' + s);
	}
    }

    public static void main(String[] args) {
	BinarySearchTree b = new BinarySearchTree();
	b.insert(5);
	b.insert(11);
	b.insert(3);
	b.insert(4);
	b.insert(12);
	b.insert(2);
	b.printPretty();
    }

}