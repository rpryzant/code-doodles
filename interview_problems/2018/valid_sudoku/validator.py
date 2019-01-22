

def isvalid(M):
    return all(
        [valid(r) for r in M] + [valid(c) for c in gen_cols(M)] + [valid(s) for s in gen_submatrices(M)]
        )

def valid(a):
    assigner = lambda x: True if x in a else False
    d = {x: assigner(x) for x in range(1,10)}
    return all(d.values())

def gen_cols(M):
    for i in range(len(M[0])):
        yield [M[k][i] for k in range(len(M))]

def gen_submatrices(M):
    for ro in range(3):
        for co in range(3):
            out = []
            for i in range(3):
                for j in range(3):
                    out.append(M[i+ro*3][j+co*3])
            yield out


test = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]
print isvalid(test)


test = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,9,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]
print isvalid(test)
