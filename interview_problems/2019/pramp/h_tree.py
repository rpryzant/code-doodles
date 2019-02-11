H tree construction


H-tree
	given
		center (x, y)
		length	
		depth
	draw h-tree centered at x, y



|-|  

depth 0? not allowed
infinite length? not possible, decreases by sqrt(2) each time



def draw_h_tree(center, length, depth):
	if depth == 0:
		return

	cx, xy = center
	lh = length / 2
	
	# center
	draw_line((cx - lh, cy), (cx + lh, cy))
# left
	draw_line((cx - lh, cy - lh), (cx - lh, cy + lh))
# right
	draw_line((cx + lh, cy - lh), (cx + lh, cy + lh))

	# h trees from corners
	next_len = length / sqrt(2)
	draw_h_trees((xc - lh, cy + lh), next_len, depth = -1)
	draw_h_trees((xc - lh, cy - lh), next_len, depth = -1)
	draw_h_trees((xc + lh, cy + lh), next_len, depth = -1)
	draw_h_trees((xc + lh, cy - lh), next_len, depth = -1)

