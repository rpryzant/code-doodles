"""
dfs

26^n

sofar (= wordlist)
i (= spot in word)

DICT = {}

better: 
BFS

even better: 
bi-BFS

"""

def successors(w, i):
    for ch in range(ord(‘a’), ord(‘b’)):
        w[i] = ch
        if w in DICT:
            yield w[:]


def ladder(start, end):
    assert len(start) == len(end)

    out = []
    dfs(sofar, i):
    if i >= len(start):
        if not out or len(sofar) < len(out):
            out = sofar
        return
    for succ in successors(sofar[-1][:], i):
        sofar.append(succ)
        dfs(sofar, i+1)
        sofar.pop()

        dfs([], 0)

    return out




DICT = set([x.strip().lower() for x in open('/usr/share/dict/words')])

from Queue import Queue



def bi_bfs(start, end):
    s_distances = {start: 0}
    qS = Queue()
    qS.put(start)

    e_distances = {end: 0}
    qE = Queue()
    qE.put(end)

    while not qS.empty() or not qE.empty():
        cur_s = qS.get()
        for succ in successors(cur_s):
            if succ in e_distances:
                return e_distances[succ] + s_distances[cur] 
            s_distances[succ] = s_distances[cur] + 1
            qS.put(succ)

        



def ladder2(start, end):
    assert len(start) == len(end)


    return bi_bfs(start, end)




