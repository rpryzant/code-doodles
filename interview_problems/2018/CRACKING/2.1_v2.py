


def rm_dups(head):
    assert head is not None

    seen = set()
    runner = head
    while runner.next != None:
        seen.add(runner.data)
        if runner.next.data in seen:
            runner.next = runner.next.next
        else:
            runner = runner.next

    return head



def rm_dups_inplace(head):
    assert head is not None

    runner = head
    while runner.next != None:
        inner_runner = runner
        while inner_runner.next != None:
            if inner_runner.next.data == runner.data:
                inner_runner.next = inner_runner.next.next
            else:
                inner_runner = inner_runner.next
        runner = runner.next

    return head
