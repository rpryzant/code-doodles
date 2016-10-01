
import re


s = "x.y.z.w:port"

print len(re.split("\.|\:", s))

