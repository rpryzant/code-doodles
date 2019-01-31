"""bisect square


both in half? 
does line need to be parallel to x axis?


do squares overlap? 


how is square structured? can i assume 
	[topleft, topright, botttomleft, bottomright]


if so, then middle coordinate is at 
	[(topleft + topright) / 2 , (bottomleft + topleft) / 2]


any line that bisects a square’s centroid splits that square in half

so any line that goes from centroid to centroid splits both in half

so """

def bisecting_line(a, b):
	pta = [(a.topleft + a.topright) / 2, (a.bottomleft, a.topleft) / 2]
	ptb = [(b.topleft + b.topright) / 2, (b.bottomleft, b.topleft) / 2]
	return pta, ptb

