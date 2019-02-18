"""

text    (str)
pattern (str) (re)

return true if text matchs pattern, false otherwise

re language:
  *, .
  any other char (literal)
  ?\w

  * = 0+ of preceeding
  . = anything
  

if there was no star:

for text_i, pattern_i in zip(text, pattern):
  if text_i != pattern_i and pattern_i != .:
    return false
return true


because there IS a star

text = "acd", pattern = "*acd"  **
text = "acd", pattern = "acd*"
text = "acd", pattern = "ab*c."
         ^                  ^

text = "acdddddde", pattern = "acd*de" --> false
                ^                  ^


time: O(n)


Input:
 



"", "a*"
^    ^

axd  ac*xd
 ^      ^

"abaa", "a.*a*"
  ^       ^

"""

def is_match(text, pattern):
  i, j = 0, 0
  while i < len(text) and j < len(pattern): 
    if j < len(pattern) - 1 and pattern[j + 1] == '*':
      while text[i] == pattern[j - 1] and i < len(text):
        i += 1
      j += 2

    else:
      if text[i] != pattern[j] and pattern[j] != '.':
        return False

      i += 1
      j += 1

  # corner case "", "a*"
  if (j == len(pattern) - 1 and pattern[j + 1] == '*') or \
     (i == len(text) and j == len(pattern)):
    return True

  return False


