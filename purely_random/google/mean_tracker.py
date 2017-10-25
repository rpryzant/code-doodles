Please use this Google doc to code during your interview. To free your hands for coding, we recommend that you use a headset or a phone with speaker option.



utility

stream coming in
want to maintain moving average of window

k = 10e^20
  = small enough that buffer fits in memory

1 [2 3 4 5] 6 7
         ^
[  1 2 3] 4 5 6 7
       ^

-always serial
-if haven’t filled “buffer” return mean of so far

what the user sees
tracker = MeanTracker(k)
for i in range(100):
    tracker.update(i)
    if i % 5 == 0:
        print tracker.get_mean()


1: soln that uses a buffer
FIFO queue 
-in our constructur, init FIFO queue
-in update: 
add to queue
if len(queue) > k:
    queue.pop()
-in get_mean:
report mean(queue)

O(k+1)space
O(k) time


2: getting rid of buffer, or maybe speeding up




“””
q = Queue()   # FIFO queue with O(1) put/get
q.put(5)
q.get()
q.peek()  => “front” element

from collecitons import deque
q = deque()
.appendleft()
.extendleft([1,2,3,4])
.pop()

“””
from Queue import Queue
from numpy import np

class MeanTracker:

    def __init__(self, k):
        assert k > 0
self.k = k
self.q = Queue()
self.sum = 0

def update(self, x):
assert isinstance(x, (float, int))
self.q.put(x)
if len(self.q) > self.k:
    self.sum -= self.q.get()
    self.sum += x

def get_mean(self):
    return None if len(q) == 0 else float(self.sum) / len(q)

space/time
O(K space)
O(1)


tracker = MeanTracker(k)
print tracker.get_mean()
=> 0

tracker = MeanTracker(k)
for i in range(100):
    tracker.update(i)
    if i % 5 == 0:
        print tracker.get_mean()




