import random

def shuffle():
    open = [i for i in range(52)]
    return [extract_index(open) for i in range(52)]

def extract_index(l):
    i = int(random.random() * len(l))
    t = l[i]
    del l[i]
    return t


def shuffle_in_place(l):
    for i in range(len(l)):
        j = int(random.random() * i)
        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp


for _ in range(5):
    print shuffle()


t = [i for i in range(1, 53)]
for _ in range(5):
    shuffle_in_place(t)
    print t
