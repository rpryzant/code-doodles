"""
Busiest Time in The Mall
The Westfield Mall management is trying to figure out what the busiest moment at the mall was last year. You’re given data extracted from the mall’s door detectors. Each data point is represented as an integer array whose size is 3. The values at indices 0, 1 and 2 are the timestamp, the count of visitors, and whether the visitors entered or exited the mall (0 for exit and 1 for entrance), respectively. Here’s an example of a data point: [ 1440084737, 4, 0 ].

Note that time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Given an array, data, of data points, write a function findBusiestPeriod that returns the time at which the mall reached its busiest moment last year. The return value is the timestamp, e.g. 1480640292. Note that if there is more than one period with the same visitor peak, return the earliest one.

Assume that the array data is sorted in an ascending order by the timestamp. Explain your solution and analyze its time and space complexities.

Example:

input:  data = [ [1487799425, 14, 1], 
                 [1487799425, 4,  0],
                 [1487799425, 2,  0],
                 [1487800378, 10, 1],
                 [1487801478, 18, 0],
                 [1487801478, 18, 1],
                 [1487901013, 1,  0],
                 [1487901211, 7,  1],
                 [1487901211, 7,  0] ]

output: 1487800378 # since the increase in the number of people
                   # in the mall is the highest at that point
Constraints:

[time limit] 5000ms

[input] array.array.integer data

1 ≤ data.length ≤ 100
[output] integer


[observations]
observation = [timestamp, group size, group movement (in 1 or out 0) ]

total = 0
for each observation in the data
  if its a new timestamp 
    look at your running total, check if max
  add the delta to a running total
if running total > max
  set max


data = [ [1487799425, 14, 1],   
         [1487799425, 4,  0],  
         [1487799425, 2,  0], 
         [1487800378, 10, 1],  
         [1487801478, 18, 0],  
         [1487801478, 18, 1],
         [1487901013, 1,  0],  
         [1487901211, 7,  1],
         [1487901211, 117,1] ] #

max     18
total   -1
"""

# [1 2 3 4 5]
#    ^
#    0 1 2 3

def gen_ts_chunks(data):
  out = [data[0]]
  for obs in data[1:]:
    if obs[0] != out[-1][0]:
      yield out
      out = [obs]
    else:
      out.append(obs)
  yield out

def fbp2(data):
  max_ts, max_total, total = None, 0, 0
  for chunk in gen_ts_chunks(data):
    total += sum([obs[1] * (1 if obs[2] else -1) for obs in chunk])
    if total > max_total:
      max_ts = chunk[0][0]
      max_total = total
  return max_ts



def find_busiest_period(data):
  max_ts = data[0][0]
  total = data[0][1] * (1 if data[0][2] else -1)
  max_total = total

  if len(data) == 1:
    return max_ts

  for i, observation in enumerate(data[1:]):
    [ts, size, movement] = observation

    if ts != data[i][0] and total > max_total:
        max_ts = data[i][0]
    total += size * (1 if movement else -1)

  if total > max_total:
    return ts
  else:
    return max_ts

print find_buisiest_period([[1487799425,21,0],[1487799427,22,1],[1487901318,7,0]])





