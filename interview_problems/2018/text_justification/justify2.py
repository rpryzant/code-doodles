# got stuck on corner cases, wasn't super areful

def justify(a, L):
    i = 0
    out = []
    while i < len(a):
        newi = take_words(a, i , L)
        new_line = pad(a[i: newi], L)
        out.append(new_line)
        i = newi
    return out

def take_words(a, i, L):
    total = 0
    j = i
    while total <= L + 1:
        if j == len(a):    # corner case
            return j
        total += len(a[j]) + 1
        j += 1
    return j - 1

def pad(chunk, L):
    npads = L - sum(map(lambda x: len(x), chunk))
    nbreaks = max(len(chunk) - 1, 1)
    pads = [' ' * (npads / nbreaks) for _ in range(nbreaks)]
    for i in range(npads % nbreaks):
        pads[i] += ' '
    return ''.join(w+p for w, p in zip(chunk, pads + ['']))






test = ["This", "is", "an", "example", "of", "text", "justification."]
print justify(test, 16)
print [len(x) for x in justify(test, 16)]

