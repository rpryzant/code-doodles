"""
GO THROUGH EXAMPLES

  1 > 2 > 3 > 4 >  5 > N
 h  t post


  2 > 1 > 3 > 4 >  5 > N
 t  h post

  2 > 1 > 3 > 4 >  5 > N
    prev   t  post
        h

  2 > 1 > 4 > 3 >  5 > N
    prev   h  post
        t
"""



def reverse(pre, head, tail, post):
    cur = head
    prev = pre
    while True:
        tmp = cur.next
        cur.next = prev

        prev = cur
        cur = tmp

        if id(prev) == id(tail):
            head.next = post
            pre.next = tail
            return head, post

def reverse_by_k(k, n):
    pre = None # or dummy, and remove at end
    head = n
    while True:  # TODO
        tail = head
    for _ in range(k-1):
        tail = getattr(tail, ‘next’, None)
        if not tail: 
            out = head
            while out.next is not None:
                out = out.next
            return out
        post = tail.next
        pre, head = reverse(pre, head, tail, post)
