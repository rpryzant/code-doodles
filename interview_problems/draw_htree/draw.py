    
import math
               
draw_htree(x, y, start_l, depth):
   if start_l < 1 or depth < 1:
      return

   if depth % 2:
      # vertical
      draw_line(x, x, y - ((start_l * 1.0) / 2),  y + (start_l / 2))
      draw_htree(x, y - ((start_l * 1.0) / 2), start_l / math.sqrt(2), depth -= 1)
      draw_htree(x, y + ((start_l * 1.0) / 2), start_l / math.sqrt(2), depth -= 1)      
   else:
      # horizontal
      draw_line(x - ((start_l * 1.0) / 2), x + (start_l / 2), y,  y)
      draw_htree(x - ((start_l * 1.0) / 2), y, start_l / math.sqrt(2), depth -= 1)
      draw_htree(x + ((start_l * 1.0) / 2), y, start_l / math.sqrt(2), depth -= 1)


def draw_line(x1, x2, y1, y2):
   pass
   
