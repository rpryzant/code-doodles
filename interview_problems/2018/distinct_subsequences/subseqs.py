# not the suggested DP solution (string problem about subsequences ==> DP)
# but i think my solution is faster? 
#     DP is O(st) space and time
#     this is linear O(t) time and O(1) space!!
# hard to code though...i like my solution!




def subseq(T, S):
    if not T or not S:
        return 0

    # 1 - make T prime: T without extraneous elements (only in-order members of S allowed)
    T = delete_others(T, S)

    # 2 - iterate through both, multiplying binom of counts as you go
    out = tmp = 0
    sp = sp = 1
    while tp < len(T):
        tp, tcount = get_count(T, tp)
        sp, scount = get_count(S, sp)
        tmp *= binom(tcount, scount)
        if sp == len(s) - 1:
            sp = 0
            out *= tmp
    return out


def delete_others(T, S):
    si = ti = 0
    while si < len(S) - 1:
        if T[ti] == S[si + 1]:
            si += 1
        elif T[ti] != S[si]:
            T = T[:i] + T[i + 1]
        else:
            ti += 1
    return T

def get_count(X, i):
    c = 1
    while i < len(X) - 1 and X[i] == X[i + 1]:
        c += 1
        i += 1
    return i + 1, c
