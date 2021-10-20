from Piece import Piece
class Pawn(Piece):

    def __init__(self, xPos, yPos, color):
        super().__init__(xPos, yPos, color)
        self.char += "P"

    def checkForAvailableMoves(self, chessboard):
        if self.color:
            if self.isAvailable(self.pos[0], self.pos[1] - 1, chessboard[int(self.color)]):
                if self.isAvailableOpponent(self.pos[0], self.pos[1] - 1, chessboard[int(not self.color)]):
                    self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0], self.pos[1] - 1]])
            if self.pos[1] == 6:
                if self.isAvailable(self.pos[0], self.pos[1] - 2, chessboard[int(self.color)]):
                    if self.isAvailableOpponent(self.pos[0], self.pos[1] - 2, chessboard[int(not self.color)]):
                        self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0], self.pos[1] - 2]])
            for i in range(-1, 2, 2):
                if self.isAvailable(self.pos[0] + i, self.pos[1] - 1, chessboard[int(self.color)]):
                    if not self.isAvailableOpponent(self.pos[0] + i, self.pos[1] - 1, chessboard[int(not self.color)]):
                        self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0] + i, self.pos[1] - 1]])
            return self.availableMoves
        else:
            if self.isAvailable(self.pos[0], self.pos[1] + 1, chessboard[int(self.color)]):
                if self.isAvailableOpponent(self.pos[0], self.pos[1] + 1, chessboard[int(not self.color)]):
                    self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0], self.pos[1] + 1]])
            if self.pos[1] == 1:
                if self.isAvailable(self.pos[0], self.pos[1] + 2, chessboard[int(self.color)]):
                    if self.isAvailableOpponent(self.pos[0], self.pos[1] + 2, chessboard[int(not self.color)]):
                        self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0], self.pos[1] + 2]])
            for i in range(-1, 2, 2):
                if self.isAvailable(self.pos[0] + i, self.pos[1] + 1, chessboard[int(self.color)]):
                    if not self.isAvailableOpponent(self.pos[0] + i, self.pos[1] + 1, chessboard[int(not self.color)]):
                        self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0] + i, self.pos[1] + 1]])
            return self.availableMoves