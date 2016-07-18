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
    struct node *next;
}node;




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
 * insert at tail of list pointed to by n
 */
void insert(node **n, int d) {
    node *new = (node *)malloc(sizeof(node));
    new -> data = d;
    new -> next = NULL;
    if ((*n) == NULL) {
	(*n) = new;
    } else {
	node *runner = (*n);
	while (runner -> next != NULL) {
	    runner = runner -> next;
	}
	runner -> next = new;
    }
}


/*
 * inserts a new node at index i
 */
void insertAt(node *n, int d, int i){
    if (n == NULL || i < 0 || i >= length(n)) {
	printf("List index out of range.");
	return;
    }
    // pre-decriment i to account for adding new to n.next
    i--;
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
 * removes node containing the target data
 */
void delete(node *n, int d) {
    if (n -> data == d) {
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
	n = n -> next;
    }
    printf("\n");
    return;
}

/*
 * reverses the list pointed to by n
 */
node *reverse(node *n) {
    node *next;
    node *prev = NULL;
    while (n) {
	next = n -> next;
	n -> next = prev;
	prev = n;
	n = next;
    }
    return prev;
}

int main() {
    int i, x, y;
    node *head = NULL;
    while (1) {
	printf("List ops:\n");
	printf("\t1. insert at tail\n");
	printf("\t2. insert at index\n");
	printf("\t3. delete by value\n");
	printf("\t4. contains value\n");
	printf("\t5. length\n");
	printf("\t6. reverse\n");
	printf("\t7. print list\n");

	scanf("%d", &i);
	if (i < 0 || i > 7) {
	    printf("%d is not a valid option.", i);
	    continue;
	} else {
	    switch(i) {
	        case 1:
		    printf("enter a number to insert:\n");
		    scanf("%d", &x);
		    insert(&head, x);
		    break;
	        case 2:
		    printf("enter a number to insert:\n");
		    scanf("%d", &x);
		    printf("enter an index to insert at:\n");
		    scanf("%d", &y);
		    if (y < 0 || y > length(head)) {
			printf("invalid index.");
			break;
		    }
		    insertAt(head, x, y);
		    break;
	        case 3:
		    printf("enter a number to delete:\n");
		    scanf("%d", &x);
		    delete(head, x);
		    break;
	        case 4:
		    printf("enter a number to test for:\n");
		    scanf("%d", &x);
		    printf("%d\n", contains(head, x));
		    break;
	        case 5:
		    printf("The length is %d.\n", length(head));
		    break;
	        case 6:
		    head = reverse(head);
		    printf("List reversed.\n");
		    break;
	        case 7:
		    print(head);
		    break;
	    }
	}
    }
}
