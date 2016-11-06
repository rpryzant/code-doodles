
"""
I like my solution to this one!! 

I haven't completely comvinced myself that it is guarenteed to be correct,
   but intuitively it makes a lot of sense. 

i guess you could say that I can't prove to myself that it works,
   but i also can't prove that it doesn't work.


My soln is as follows:

1) calculate a difference vector that shows how your gas level will change
    as you go from station i to station i+1.

2) zip through this difference vector and replace elmenets with partial sums
    it now shows your gas level as if you started a circuit at station 0

3) find where you'd have "peak" gas levels, then backtrack until you get to the 
    bottom of that monotomically increasing sequence of gas levels

4) return that bottom point


I think this works because if you're going to make it around the circuit,
   you can't do any better than if you started at the first of a sequence
   of stations which would eventually get your tank to the highest level
   it can possibly get to. 


Might be thrown off by circular nature of the problem, e.g. what if 
   increasing subsequence straddles the endpoints of the dG list
But in that casethe algoirthm would loop around

"""


def gas_stations(G, C):
    dG = [sum(pair) for pair in zip(G, C)]

    for i in range(1, len(dG)):
        dG[i] = dG[i-1] + dG[i]

    maxi = max((x, i) for i, x in enumerate(dG))[1]

    while dG[::-1][(maxi + 1) % len(dG)] < dG[maxi]:
        maxi = maxi - 1 if maxi > 0 else len(dG) - 1

    return maxi



print gas_stations([1,2],[2,1])
print gas_stations([5, 5,5,5,5,5,5], [-8,-4,0,-7,-5,-5,2])
