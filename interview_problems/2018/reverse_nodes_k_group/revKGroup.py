#phew.... this was really tough to code.
# not sure if it even works...afraid to test
# note:
########  
#               {cut/reverse section}
#      left stump  l cut      r cut    r stump
#    ...  [] -> {  <-[] ...  <-[]   }   [] -> ...
#         lc.next        lc         rc        rs
#



def KLeft(n, k):
    for _ in range(k-1):
        if n is None:
            return False
        n = n.next
    return True

def reverseK(n, k, prev):
    for _ in range(k):
        tmp = n.next
        n.next = prev
        prev = n
        n = tmp
    return prev, n

def revKChunks(n, k):
    hptr = Node(0)
    hptr.next = n

    ls = Node(0)
    ls.next = n
    lc = n
    while kLeft(n, k):
        # flip around the next chunk
        tmp = ls
        rs, rc = revK(n, k, tmp)
        # hook up newly flipped chunk in the right direction, reset tracking ptrs
        lc.next.next = rc
        lc.next = rs
        lc = rs
        n = rs
    # retrieve head and return
    # TODO: THIS IS BLATANTLY WRONG...GET REAL HEAD
    n = hptrp.next
    hptr.next = None
    return n
        

