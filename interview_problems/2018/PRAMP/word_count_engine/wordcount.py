import re
import string
from collections import Counter

def wordcount(doc):
    doc = doc.lower()
    doc = re.sub('[%s]' % string.punctuation, '', doc)
    counts = Counter(doc.split())
    out = [[w, str(cnt)] for w, cnt in counts.most_common()]
    return out



test = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
print wordcount(test)
