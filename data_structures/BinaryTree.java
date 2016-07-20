import java.util.*;
import java.lang.*;

class Node {
    public int data;
    public Node left;
    public Node right;

    Node(int data) {
	this.data = data;
	this.left = null;
	this.right = null;
    }
}


public class BinaryTree {
    public int size;
    public Node root;

    BinaryTree() {
	this.size = 0;
	this.root = null;
    }

    public int getSize() {
	return size;
    }

    public void insert(int x) {
	insertR(root, x);
    }

    private void insertR(Node root, int x) {
	if (root == null) {
	    size++;
	    root = new Node(x);
	} else if (x < root.data) {
	    insertR(root.left, x);
	} else {
	    insertR(root.right, x);
	}
    }

    public void delete(int x) {
	deleteR(root, x);
    }
    
    private void deleteR(Node root, int x) {
	if (x < root.data) {
	    deleteR(root.left, x);
	} else if (x > root.data) {
	    deleteR(root.right, x);
	}
	if (root.left == null && root.right == null) {
	    root = null;
	} else if (root.left != null) {
	    root.data = root.left.data;
	    root.left = null;
	} else if (root.right != null) {
	    root.data = root.right.data;
	    root.right = null;
	} else {
	    Node min = findMin(root.right);
	    root.data = min.data;
	    min = null;
	}
    }

    public Node findMin(Node root) {
	if (root.left == null) {
	    return root;
	} else {
	    return findMin(root.left);
	}
    }
    
}

