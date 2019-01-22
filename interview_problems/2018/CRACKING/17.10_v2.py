"""
BF: 
sort, return mid element
n log n time, good on space

are negatives allowed?
how big is the array? 

subproblems?


THIS ONE IS AWESOME!!!!!!!
(i had to read the solution, but i really got it this time vs last
   time i was a little confused)

"""


def find_majority(a):
    def float():
        # float through a, holding on to each candidate as long
        # as it's sticking around
        candidate = a[0]
        count = 1
        for x in a[1:]:
            if count == 0:
                candidate = x
            if x == candidate:
                count += 1
            else:
                count -= 1
        return candidate

    def validate(x):
        return sum(1 if q == x else 0 for q in a) > len(a) / 2

    out = float()
    return out if validate(out) else -1



print find_majority([1,2,5,9,5,9,5,5,5])
