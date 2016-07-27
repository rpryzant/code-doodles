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

    public boolean hasBothChildren() {
	return (this.left != null && this.right != null);
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
	deleteR(null, root, false, d);
    }

    private void deleteR(Node parent, Node current, boolean isLeft, int d) {
	if (current == null) {
	    return;
	} else if (current.data == d) {
	    if (current.hasNoChildren()) {
		if (isLeft)
		    parent.left = null;
		else
		    parent.right = null;
	    } else if (current.hasBothChildren()) {
		int min = getMin(current.right);
		delete(min);
		current.data = min;		
	    } else if (current.left != null) {
		if (isLeft)
		    parent.left = parent.left.left;
		else
		    parent.right = parent.right.left;
	    } else if (current.right != null) {
		if (isLeft)
		    parent.left = parent.left.right;
		else
		    parent.right = parent.right.right;
	    }
	} else if (current.data > d) {
	    deleteR(current, current.left, true, d);
	} else {
	    deleteR(current, current.right, false, d);
	}
    }

    private int getMin(Node n) {
	if (n == null) {
	    return -1;
	} else if (n.left == null) {
	    return n.data;
	} else {
	    return getMin(n.left);
	}
    }

    public boolean DFS(int t) {
	return DFS(root, t);
    }

    public boolean DFS(Node n, int t) {
	if (n == null) {
	    return false;
	}
	if (n.data == t) {
	    return true;
	}
	return DFS(n.left, t) || DFS(n.right, t);
    } 

    public boolean BFS(int t) {
	Queue<Node> q = new PriorityQueue<Node>();
	q.add(root);
	Node current;
	while (!q.isEmpty()) {
	    current = q.remove();
	    if (current.data == t)
		return true;
	    q.add(current.left);
	    q.add(current.right);
	}
	return false;
    } 


    public void printPretty() {
	System.out.println('\n');
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
	b.delete(5);
	b.printPretty();
	System.out.println(b.DFS(5));
	System.out.println(b.DFS(3));
	System.out.println(b.DFS(5));
	System.out.println(b.DFS(3));
    }
}