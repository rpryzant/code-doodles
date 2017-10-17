"""
lowercase \w

word encription:
1  char => ord(char)
2  first letter += 1
3  w[1:] gets previous added
4  sub 26 until in range a-z
5  convert back to letters


5 
  nums = [ord(c) for c in w]
4 
  def bump(x):
    while x < ord('z'):
      x += 26
    return x

  nums = map(lambda x: x if x <= ord('z') else bump(x), nums)
  
3
  nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]

2
  nums[0] -= 1

1
  out = [ord(x) for x in nums]


chr(int) ==> 'a'



[z    ch           ch2]
 z+1  (ch+z+1)  ch2 + (ch+z+1)

  
[c  a   t]

"""

def bump(x):
  while x < ord('z'):
    x += 26
  return x


def decrypt(word):
  assert len(word) > 0 and word.isalpha()
  nums = [ord(c) for c in word]

  nums0 = bump(nums[0]) if nums[0] == ord('a') else nums[0]
  nums = nums[0] + map(lambda x: bump(x), nums[1:])

  nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]

  nums[0] -= 1
  return ''.join(chr(x) for x in nums)

