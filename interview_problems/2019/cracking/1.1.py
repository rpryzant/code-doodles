from collections import Counter

def is_unique(s):
    return sum(Counter(s).values()) == len(s)
