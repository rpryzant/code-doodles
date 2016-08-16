import re

def strstr(s, sub):
    pattern = re.compile(sub + '.*')
    for m in pattern.finditer(s):
        return m.start()
    return -1


t = 'one two three'
print strstr(t, 'two')
print strstr(t, 'five')
print strstr(t, '')

