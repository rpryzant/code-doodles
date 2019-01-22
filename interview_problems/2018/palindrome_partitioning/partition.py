# in notes


def isPalin(s):
    return s == s[::-1]

def palinPartition(s):
    if not s:
        return []
    out = []

    def dfs(i, sofar):
        if i == len(s):
            out.append(sofar[:])
            return
        for j in range(i+1, len(s)+1):
            chunk = s[i:j]
            if isPalin(chunk):
                sofar.append(chunk)
                dfs(j, sofar)
                sofar.pop()

    dfs(0, [])
    return out

print palinPartition('aab')
