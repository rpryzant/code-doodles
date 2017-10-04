"""
fuck yeah!!!! nailed it

have:
rand5() ==> [0, 4]

want:
rand7() ==> [0, 6]

operations: +, *, /, %

ATTEMPT 1
multiple passes:
== pass 1:
rand5() * 7
[0 4]
[5 9]
[10 14] 
...

== pass 2:
prev + rand5()

problem: rand5()*7 means some ranges will get skipped
  ==> soln i think we can pack this densly with rand5() * 5
[0 4]
[5 9]
[10 14] 
[15 19]
[20 24]

problem: 22-24 are OOB (unequal probs if i mod it)
  ==> soln just resample from the start if you hit that range

fun obseration: we can probably make this arbitrary, but lets think about that later

"""
import random


def rand5():
    return random.choice(range(5))


def rand7(rand5):
    i = (rand5() * 5) + rand5()
    while i > 21:
        i = (rand5() * 5) + rand5()
    return i





def randN(rand, n, tgt):
    i = (rand() * n) + rand()
    closest_tgt_multiple = int((n*n)/tgt) * tgt
    while i > closest_tgt_multiple:
        i = (rand() * n) + rand()
    return i


from collections import defaultdict
counts = defaultdict(int)
for _ in range(10000):
    counts[randN(rand5, 5, 7)] += 1
print counts
