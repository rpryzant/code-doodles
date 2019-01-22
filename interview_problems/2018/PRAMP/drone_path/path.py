"""
burns 1 per ascend
gains 1 per descend

(x, y, z)

min_energy(route)  ==> mininmal energy


maintain "energy left" counter (initialize to 0)
go through route


max(0, -lowest point) =     what you want to start with
                            to end with something close to 0

(z)


10, 0, 6, 15, 8

0  10  4   -5  2
       ^
0

1: 0 - (0 - 10)
2: remaining[i] - (6 - 0)
                   z - route[i-1]

hell?


 
[[0,2,6],[10,10,20]]

[6    20]
 0 
 
0    20

0   - (20 - 6)
-14


1
4

0

"""


def calc_drone_min_energy(route):
  remaining = [0]
  for i, [_, _, z] in enumerate(route[1:]):
    remaining.append(remaining[i] - (z - route[i][2]))
  return max(0, -min(remaining))



def calc_drone_min_energy(route):
  min_tank = 0
  cur_tank = 0
  for i, [_, _, z] in enumerate(route[1:]):
    cur_tank = cur_tank - (z - route[i][2])
    min_tank = min(min_tank, cur_tank)
  return -min_tank




route = [ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]
#route = [[0,2,6],[10,10,20]]
print calc_drone_min_energy(route)


