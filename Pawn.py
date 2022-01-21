from Piece import Piece
import colorama


class Pawn(Piece):

    def __init__(self, xPos, yPos, color):
        """
        New Pawn Piece at position xPos, yPos, and the color"""
        super().__init__(xPos, yPos, color)
        self.char += "P" + colorama.Style.RESET_ALL

    def __str__(self):
        """
        Sets the String of the Object to its char, so I can access it with str()"""
        return self.char

    def checkForAvailableMoves(self, chessboard):
        """
        Checks for the available moves from this piece"""
        self.availableMoves = []
        if self.color:
            if self.isAvailable(self.pos[0], self.pos[1] - 1, chessboard[int(self.color)]):
                if self.isAvailable(self.pos[0], self.pos[1] - 1, chessboard[int(not self.color)]):
                    self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0], self.pos[1] - 1]])
            if not self.moved:
                if self.isAvailable(self.pos[0], self.pos[1] - 2, chessboard[int(self.color)]):
                    if self.isAvailable(self.pos[0], self.pos[1] - 2, chessboard[int(not self.color)]):
                        self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0], self.pos[1] - 2]])
            for i in range(-1, 2, 2):
                if self.isAvailable(self.pos[0] + i, self.pos[1] - 1, chessboard[int(self.color)]):
                    if not self.isAvailable(self.pos[0] + i, self.pos[1] - 1, chessboard[int(not self.color)]):
                        self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0] + i, self.pos[1] - 1]])
            return self.availableMoves
        else:
            if self.isAvailable(self.pos[0], self.pos[1] + 1, chessboard[int(self.color)]):
                if self.isAvailable(self.pos[0], self.pos[1] + 1, chessboard[int(not self.color)]):
                    self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0], self.pos[1] + 1]])
            if not self.moved:
                if self.isAvailable(self.pos[0], self.pos[1] + 2, chessboard[int(self.color)]):
                    if self.isAvailable(self.pos[0], self.pos[1] + 2, chessboard[int(not self.color)]):
                        self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0], self.pos[1] + 2]])
            for i in range(-1, 2, 2):
                if self.isAvailable(self.pos[0] + i, self.pos[1] + 1, chessboard[int(self.color)]):
                    if not self.isAvailable(self.pos[0] + i, self.pos[1] + 1, chessboard[int(not self.color)]):
                        self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0] + i, self.pos[1] + 1]])
            return self.availableMoves
