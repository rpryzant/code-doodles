


def reverse(head):
    if head is None:
        return head
    cur = head
    prev = None
    
    while cur is not None:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    return prev
        
