"""
insertion sort

two variabls: min, index

1) move [:index] elements to 2nd stack
2) find min in remaining stack (moving elemnts to 2nd stack)
3) transfer back to original stack, but pluck out the min and move it to the index^th spot
4) increment index

O(n^2) but who'se counting??


struggled with this more than i should have....

"""
import sys

class Stack:
    def __init__(self, l=[]):
        self.d = l

    def push(self, x):
        self.d.append(x)

    def pop(self):
        if not self.d:
            raise Exception('pop from empty stack')
        return self.d.pop()

    def peek(self):
        return self.d[-1]

    def isEmpty(self):
        return len(self.d) == 0



def percolate(s, aux):
    top = s.pop()
    done = True
    while not s.isEmpty():
        if top <= s.peek():
            aux.push(top)
            top = s.pop()
        else:
            done = False
            aux.push(s.pop())
    aux.push(top)
    return done

def transfer(a, b):
    while not a.isEmpty():
        b.push(a.pop())

def sort_stack(s):
    aux = Stack()
    while not percolate(s, aux):
        transfer(aux, s)
    transfer(aux, s)
    return s

s = Stack([5,2,6,2,1,1])
s = sort_stack(s)
print s.d





