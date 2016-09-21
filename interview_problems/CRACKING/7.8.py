"""
BRAINSTORMING:

OBJECTS
   -piece
   -board
   -game
   -user
   -user manager

ACTIONS
   -piece
      -flip
      -isCaptured
      -get player
   -board
      -place
      get valid moves
   -game
      is valid move
      make move
      is done
   -user
      wins
      losses
      getpiece
      main method (game engine)
   -usermanager
      makeuser
      leaderboard
      getuser

STATE
   -piece
      user id
      side info?
   -board
      2d array for pieces
   -game
      coords of valid moves
      scores
      [] users
    -user
       pieces[]
       id
    -manager
       {uid: user}
       sorted leaderboard? 

"""


class game:
    def __init__(self, u1, u2, m=20, n=20):
        self.users = [u1, u2]
        self.board = Board(m, n)
        self.validmoves = [(r, c) for r in range(m) for c in range(n)]
        self.scores = [0,0]

    def makemove(self, m, n, piece):
        if (m, n) in self.validmoves:
            return (), false
        del self.validmoves[Utils.get_index((m, n), self.validmoves)]
        return self.board.place(m, n, piece), True

    def main(self):
        i = 0
        while not self.board.done() and not any(map(lambda x: not x.done(), self.users)):
            move = False, ()
            while not move[0]:
                c = self.users[i % 2].getmove()
                move = self.makemove(*c)
                self.scores[i % 2] += move[1]
                i += 1


class board:
    def __init__(self, ...):
        # instance variables, data, board grid
    
    def place(self, r, c, piece):
        s = 0
        self.b[r][c] = piece
        # check above
        # if r is big enough, there's a piece 2 spots above, there's a piece 1 spot above, the piece 2 
        # spots above is the same color as the recently placed piece and the piece 1 spot above is 
        # a different color, flip it!

        # same for right, left, below, etc. 

