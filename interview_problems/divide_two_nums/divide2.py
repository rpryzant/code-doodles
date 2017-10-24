"""
a / b

whole number division?
YES

fractions?
decimal remainder?


divide by 0? 
   max int

a/b = # of times b goes into a . (# of times b/10 goes into remainder) + (# times b/100 ...)

5/2

5/-2
-2 / 5
-2 / -5


check for bad input
fit as many b's into a as possible
return result if proper, -result otherwise


i, out = 0, 0
while out + b < a:
   out += b
   i += 1

if a < 0 and b < 0 or a > 0 and b > 0:
   return i
return -i

"""

def divide(a, b):
    if b == 0:
        return

    i, sofar = 0, 0
    while sofar + b < a:
        sofar += b
        i += 1

    if (a < 0 and b < 0) or (a > 0 and b > 0):
        return i
    else:
        return -i



