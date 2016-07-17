/*
 *     Brief implementation of a singly linked list
 *
 *
 *
 */ 

#include <stdio.h>
#include <stdlib.h>


typedef struct node {
    int data;
    struct node next;
}node;


/*
 * insert at tail of list pointed to by n
 */
void insert(node *n, int d) {
    while (n -> next != NULL) {
	n = -> next;
    }
    n -> next = (node *)malloc(sizeof(node));
    n = n -> next;
    n -> data = d;
    n -> next = NULL;
}


/*
 * gets the length of a ll
 */
int length(node *n){
    int i = 0;
    while (n != NULL) {
	n = n -> next;
	i += 1;
    }
    return i;
}

/*
 * inserts a new node at index i
 */
void insertAt(node *n, int d, int i){
    if (i < 0 || i >= length(n)) {
	printf("List index out of range.");
	return;
    }
    while (i > 0){
	n = n -> next;
	i--;
    }
    node *new = (node *)malloc(sizeof(node));
    new -> data = d;
    new -> next = n -> next;
    n -> next = new;
}

/*
 * tests whether the list pointed to by n contains the target value
 */
int contains(node *n, int t) {
    while (n != NULL) {
	if (n -> data == t)
	    return 1;
	n = n -> next;
    }
    return 0;
}

/*
 * removes node containing the target data
 */
void delete(node *n, int d) {
    if (n -> data == t) {
	n = n -> next;
	return;
    }
    
    while (n -> next != NULL && (n -> next) -> data != d) {
	n = n -> next;
    }
    
    if (n -> next == NULL) {
	printf("No node with data %d in this list!\n", d);
	return;
    }
    
    node *tmp; 
    tmp = n -> next;
    n -> next = (n -> next) -> next;
    free(tmp);
    return;
}

/*
 * Prints the ll pointed to by n
 */
void print(node *n) {
    while (n != NULL) {
	printf("%d\n", n -> data);
    }
    printf("\n");
    return;
}

/*
 * reverses the list pointed to by n
 */
void reverse(node *n) {
    node *next;
    node *prev = NULL;
    while(n) {
	next = n -> next;
	n -> next = prev;
	prev = n;
	n = next;
    }
    return prev;
}

