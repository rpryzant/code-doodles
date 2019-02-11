"""
drone flight planner

minimum amount of energy for drone to complete flight
	burns 1 per ascend
	gains 1 per descend
	sideways is 0

given 
	route: array( triples )
	e.g. route = [ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]

calc:
	min energy drone needs to start the route


can you move up/down multiple times?
what if route is just descent? just ascent?
route is empty?
route is 1 point?

x, y doesn’t matter

IDEA 1:
	loop through route, calc running total as if you started with a
	tank of 0

	remember the min value. 

	if min less than 0 return abs(min) else return 0

correct? yes, guarentees that you’ll get though the route, and if there was a smaller number you would ahve picked up on it
"""
def min_fuel(route):
	temp_min = 0
	cur_fuel = 0
	for i, [_, _, z] in enumerate(route[1:]):
		cur_fuel += (z - route[i][-1])
		temp_min = min(temp_min, cur_fuel)

	return abs(temp_min)
