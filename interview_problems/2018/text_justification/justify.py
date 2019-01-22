

def justify(words, L):
    if not words:
        return ""
    s = []
    i = 0
    while i < len(words):
        chunk, i = next_line(words, i, L)
        s.append(''.join(w for w in pad(chunk, L)))
    return s

def next_line(words, i, L):
    j = i + 1
    l = len(words[i]) + 1
    while l <= L and j < len(words):
        l += len(words[j]) + 1
        j += 1
    if j == len(words) and l <= L:
        return words[i:j], j
    else:
        return words[i:j-1], j - 1

def pad(chunk, L):
    i = 0
    l = sum(map(lambda x: len(x), chunk))
    while l < L:
        if len(chunk) > 1:
            chunk[i % (len(chunk) - 1)] += " "
        else:
            chunk[0] += " "
        i += 1
        l += 1
    return chunk

test = ["This", "is", "an", "example", "of", "text", "justification."]
print justify(test, 16)
