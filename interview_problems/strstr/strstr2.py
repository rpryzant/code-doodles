

def substr(s, sub):
    sub_hash = hash(sub)
    for i in range(len(s) - len(sub)):
        if hash(s[i:i+len(sub)]) == sub_hash:
            return i
    return -1


t = 'one two three'
print substr(t, 'two')
print substr(t, 'five')
print substr(t, '')




