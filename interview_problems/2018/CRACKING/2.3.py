# in notes

def delete(n):
    if n is None or n.next is None:
        return False
    n.data = n.next.data
    tmp = n.next
    n.next = n.next.next
    tmp.next = None
    return True
               
