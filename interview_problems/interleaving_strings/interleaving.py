# i like my solution to this one!

def is_interleaving(s1, s2, s3):
    def ii(s1, s2):
        m, n = len(s1), len(s2)
        if not len(s3) == m + n:
            return False
        if s1 is '' and not s2 == s3:
            return False
        if s2 is '' and not s1 == s3:
            return False
        if s3 is '' and not s1 == s2 == '':
            return False

        p1 = p2 = -1
        for i in range(len(s3)):
            if p1 < m - 1 and s1[p1 + 1] == s3[i]:
                p1 += 1
            elif p2 < n - 1 and s2[p2 + 1] == s3[i]:
                p2 += 1
        if p1 == m - 1 and p2 == n - 1:
            return True
    
        return False

    return ii(s1, s2) or ii(s2, s1)


print is_interleaving('abc', 'xyz', 'abxcyz')
print is_interleaving('abc', 'xyz', 'abxccyz')

print is_interleaving('aabcc', 'dbbca', 'aadbbcbcac')
print is_interleaving('aabcc', 'dbbca', 'aadbbbaccc')
