


def rm_dups(head):
    r = head
    d = {r.data: True}
    while r.next is not None:
        if d.get(r.next.data, False):
            r.next = r.next.next
        else:
            d[r.next.data] = True
            r = r.next

def rm_dups_nospace(head):
    cur = head
    while cur.next != null:
        r = cur
        while r.next != null:
            if r.next.data == cur.data:
                r.next = r.next.next
            else:
                r = r.next
        cur = cur.next
