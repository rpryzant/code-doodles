

class ORIENTATION():
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"
    
    @staticmethod
    def getOpposite(type):
        #dict to give opposite
        return

class SHAPE():
    INNER = # ..
    OUTER = # ..
    FLAT = # ..


class Puzzle():

    def __init__(self, size, pieces):
        self.pieces = pieces
        self.m = size
        self.n = size
        self.board = [[None for _ in range(self.n)] for _ in range(self.m)]

    # find piece that should go in row, col
    def findAndFit(self, pieces, row, col):
        # 
        return
    
    # given the board and peices, solve the game
    def solve(self):
        return
        

class Piece():
    def __init__(self, edges):
        self.edges = {
            ORIENTATION.LEFT: edges[0],
            ORIENTATION.RIGHT: edges[1],
            # ...
        }
        self.row = None
        self.col = None

    # rotate self.edge by 90 degrees
    def rotate(self):
        return

    def isCorner(self):
        return

    def isBorder(self):
        return

class Edge():
    def __init__(self, shape):
        self.shape = shape
        self.parent_piece = None

    # fits with another edge??
    def fits_with(other):
        return
