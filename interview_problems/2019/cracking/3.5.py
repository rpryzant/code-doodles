sort stack


sort stack (with an extra stack)

stack is 
push
pop
peek
isempty




allowed tmp variables?


O(N^2)

stack1 => stack2  -- put max in tmp
max on stack1
stack2 => stack1
stack1[1:] => stack2 --put max in tmp
...repeat


can reduce by constant (just have multiple tmp’s)


a little faster by percolating instead of max each time
during st1 => st2 transfer, hold on to big values as you’re going through



def percolate(s1, tmp):
    x = s1.pop()
    done = True
    for _ in range(len(s1)):
        y = s1.pop()
        if y > x:
            done = False
            tmp.append(x)
            x = y
        else:
            tmp.append(y)
    tmp.append(x)
    return done
            
def transfer(s1, s2):
    for _ in range(len(s1)):
        s2.append(s1.pop())

def sort(stack):
    tmp = []
    done = False
    while not done:
        done = percolate(s1, tmp)
        transfer(tmp, s1)
        


