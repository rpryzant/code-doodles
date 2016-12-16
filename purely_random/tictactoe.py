from random import choice
from sys import argv

# helper function to quickly generate a game's worth of coordinates
def initAvailable():
    return [(x, y) for x in range(3) for y in range(3)]

# make a move for a player, given the available board spots
def makeMove(player, board, available):
    # if there aren't any available spots, no move is possible
    if available == []: return None
    # randomly choose a spot, move there, and return its coordinates
    coord = choice(available)
    available.remove(coord)
    board[coord] = player
    return coord

# check to see if the last move was a win, given the current board
def checkWin(move, board):
    # if no move was possible, it's a tie!
    if not move: return "T"
    # otherwise check forward & reverse diagonals, horizontal & vertical lines
    x,y = move
    if   x == y and board.get((0,0)) == board.get((1,1)) == board.get((2,2)) or \
       x+y == 2 and board.get((0,2)) == board.get((1,1)) == board.get((2,0)) or \
                    board.get((0,y)) == board.get((1,y)) == board.get((2,y)) or \
                    board.get((x,0)) == board.get((x,1)) == board.get((x,2)):
        return board.get(move)
    # otherwise nobody's one yet so return nothing
    return None

# play a game!
def playGame(A, B, available):
    board = {}
    move = makeMove(A, board, available)
    while not checkWin(move, board):
        move = makeMove(B, board, available)
        if checkWin(move, board): 
            break
        move = makeMove(A, board, available)
    # return the last made move. if there is no such move, return T for 'tie'
    return board.get(move, 'T') 

# player A is X's, player B is O's
A,B = 'X','O'
g = {A: 0, B: 0, 'T': 0}
n = int(argv[1])
# play n rounds of the game
for _ in range(n):    
    g[playGame(A, B,initAvailable())] += 1
# report results
for type in g:
    print "%s happened %s%% of the time.\n" % (type, round(g[type]/float(n), 4))
