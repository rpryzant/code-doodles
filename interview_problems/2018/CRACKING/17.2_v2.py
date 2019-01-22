"""
shuffle a deck of cards                                                                                                                                                                        
input ==> output are both permutations of the deck,                                                                                                                                              and each of the 52! are represented with same prob                                                                                                                                       

we are given random()                                                                                                                                                                          

are we running this once? or many times?
                                                                                                                              

1 brute force: computer all perms then use random gen to pick one
52!

2 for each element in deck,
swap with random partner before it
O(52)

"""

def shuffle(deck):
    assert len(deck) == 52

    def swap(i, j):
        tmp = deck[j]
        deck[j] = deck[i]
        deck[i] = tmp

    for i in range(len(deck)):
        swap(i, random() * i)
