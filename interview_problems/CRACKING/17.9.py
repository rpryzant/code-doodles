# TODO - make this work! I think my idea is correct...


def gen_multiple():
    candidates = [(1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (1,1,1), (0,1,1),
                  (-1,1,0), (1,-1,0), (1,0,-1),
                  (-1,0,1), (0,-1,1), (0,1,-1)]

    yield 1
    yield 3
    prev_move = (1,0,0)
    prev_state = (1,0,0)

    while True:
        start_state = reverse(prev_state, prev_move)
        print 'start state %s' % str(start_state)
        valid_moves = [move for move in candidates if move != prev_move]
        valid_states = map(lambda x: tuple(sum(y) for y in zip(start_state, x)), valid_moves)
        minimum = None
        for i, end_state in enumerate(valid_states):
            if any(filter(lambda x: x < 0, end_state)):
                continue
            val = (3 ** end_state[0]) * (5**end_state[1]) * (7**end_state[2])
            print val
            if not minimum or val < minimum:
                minimum = val
                prev_move = get_move(prev_state, end_state)
                prev_state = end_state
        print 'prev_move %s' % str(prev_move)
        print 'prev state %s' % str(prev_state)
        print '=====> %s' % minimum
        yield minimum



def reverse(state, move):
    return tuple(si - mi for si, mi in zip(state, move))

def get_move(state1, state2):
    return tuple(s2i - s1i for s1i, s2i in zip(state1, state2))

def find_kth_multiple(k):
    i = 0
    for x in gen_multiple():
#        print i, x
        if i == k:
            return x
        i += 1


print find_kth_multiple(0)

print find_kth_multiple(8)
