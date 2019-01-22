# i like my solution to this one!






class CharStore:
    def __init__(self, T):
        self.d = {x: -1 for x in T}
        self.cnt = 0
        self.tgt = len(T)

    def has(self, c):
        return True if self.d.get(c, None) is not None else False

    # pre: c in self.d
    def set(self, c, i):
        if self.d[c] == -1:
            self.cnt += 1
        self.d[c] = i

    def complete(self):
        return self.cnt == self.tgt

    def get_chunk(self):
        if self.complete():
            return min(self.d.values()), max(self.d.values())
        return None


def window(S, T):
    min = -1
    chunk = None
    dT = CharStore(T)
    for i, c, in enumerate(S):
        if dT.has(c):
            dT.set(c, i)
            if dT.complete():
                ch = dT.get_chunk()
                if not chunk or (ch[1] - ch[0]) < min:
                    min = ch[1] - ch[0]
                    chunk = ch
    return S[chunk[0] : chunk[1] + 1] if min -1 else None


test = 'ADOBECODEBANC'
testt = 'ABC'

print window(test, testt)
