"""

can we assume this directed graph has a loop? yes


1) O(n) space O(n) time: track id(node) as you go, return first repeat :) 


2) runner that moves 2x the speed of lagger, find where they meet 

    k nodes before loop
    when slow enters loop, runner is K steps ahead, and 
        the two are LOOP_SIZE - mod(loop size, k) nodes apart from each other
    when slow and fast collide they are K away from the start ??????
    so when slow and fast collide, move slow to start and start moving fast at normal speed



3) go until first meeting, then start tracking id's
     O(n) O(k) space
"""

def find_loop(head):
    seen = set()
    runner = head
    while id(runner) not in seen:
        seen.add(id(runner))
        runner = runner.next
    return id(runner)








