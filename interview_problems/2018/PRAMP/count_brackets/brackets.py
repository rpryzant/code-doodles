
def bracket_match(text):
  if text == '':
    return 0
  elif len(text) == 1:
    return 1
  elif len(text) == 2 and text == ')(':
    return 2
  elif text[0] == ')':
    return 1 + bracket_match(text[1:])
  elif text[-1] == '(':
    return 1 + bracket_match(text[:-1])
  elif text[:2] == '()':
    return bracket_match(text[2:])
  elif text[-2:] == '()':
    return bracket_match(text[:-2])    
  else:
    return bracket_match(text[1:-1])


OPENING = '('

#( )  ) (
#1 0 -1 0



def count_brackets(text):
    needed = 0
    c = 0
    for i, ch in enumerate(text):
        if ch == OPENING:
            c += 1
        else:
            c -= 1
        if c < 0 or (i == len(text)- 1 and ch == '('):
            needed += 1
    return needed + 1 if c > 0 else needed


#print bracket_match("())(")
print count_brackets("())(")
print count_brackets("()(")
print count_brackets("())")
print count_brackets("(()")
print count_brackets("())")
print count_brackets("()(())")
