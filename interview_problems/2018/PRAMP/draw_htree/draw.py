"""
hey just got back
sure, then i'll start


task: 
  given center c, depth d, length l, 
  use drawLine to draw h-tree of depth d, centered at c


drawLine(p1, p2)
  
drawing a single h-tree:
  
drawH(c, l):
  draw middle bar using horizontal
  draw sides of h from endpoints of horizontal
  give endpoints of these sides to other recursive calls

4^{d-1}

d

"""

def drawLine((x1, y1), (x2, y2)):
    # draws line, assume implementation available
    pass

import math


def drawHTree(c, l, d):
  assert l > 0

  if d == 0:
    return

  cx, cy = c
  lh = float(l) / 2

  # middle bar
  drawLine(
    (cx - lh, cy), 
    (cx + lh, cy))

  # top bars
  drawline(
    (cx - lh, cy + lh),
    (cx - lh, cy - lh))  
  drawline(
    (cx + lh, cy + lh),
    (cx + lh, cy - lh))  

  drawHTree((cx - lh, cy + lh), l / math.sqrt(2), d - 1)
  drawHTree((cx - lh, cy - lh), l / math.sqrt(2), d - 1)
  drawHTree((cx + lh, cy + lh), l / math.sqrt(2), d - 1)
  drawHTree((cx + lh, cy - lh), l / math.sqrt(2), d - 1)  

print "Practice makes Perfect!"   
print(5/math.sqrt(2))
