import re


def len_fast(s):
    words = re.findall("[^ ]+", s)
    return len(words[-1]) if len(words) > 0 else 0

def len_better(s):
    count = 0
    counting = False
    i = len(s) - 1
    while i != 0:
        if not counting and s[i] != 0:
            counting = True
        if counting:
            if s[i] != " ":
                count += 1
            else:
                return count
        i -= 1
    return 0


print len_fast("hello world")
print len_better("hello world")
            


print len_fast("    ")
print len_better("   ")
            
