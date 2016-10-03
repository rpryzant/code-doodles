"""
E[ratio] = E[num boys before first girl] : 1

E[num boys] = P(girl right away) * (num boys if girl right away) + P(boy right away) * (num boys if boy right away)
            = (1/2)(0) + (1/2) (E + 1)
      E / 2 = 1 / 2
         E  =  1

E[ratio] = 1:1!

"""








import random



def birth():
    if random.random() < 0.5:
        return 'b'
    return 'g'


num_boys = 0
num_girls = 0

for _ in range(100000):
    children = [birth()]
    while children[-1] == 'b':
        children.append(birth())
    num_boys += len(children) - 1
    num_girls += 1

print num_boys * 1.0 /  num_girls
