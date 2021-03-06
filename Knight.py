from Piece import Piece
import colorama


class Knight(Piece):

    def __init__(self, xPos, yPos, color):
        """
        New Knight Piece at position xPos, yPos, and the color"""
        super().__init__(xPos, yPos, color)
        self.char += "N" + colorama.Style.RESET_ALL

    def __str__(self):
        """
        Sets the String of the Object to its char, so I can access it with str()"""
        return self.char

    def checkForAvailableMoves(self, chessboard):
        """
        Checks for the available moves from this piece"""
        self.availableMoves = []
        moveOffsetOptions = [-2, -1, 1, 2]
        for i in range(len(moveOffsetOptions)):
            for j in range(len(moveOffsetOptions)):
                currentOffsetX = moveOffsetOptions[i]
                currentOffsetY = moveOffsetOptions[j]
                if abs(currentOffsetX) == abs(currentOffsetY):
                    continue
                while True:
                    if self.isAvailable(self.pos[0] + currentOffsetX, self.pos[1] + currentOffsetY,
                                        chessboard[int(self.color)]):
                        self.availableMoves.append(
                            [[self.pos[0], self.pos[1]], [self.pos[0] + currentOffsetX, self.pos[1] + currentOffsetY]])
                        break
                    else:
                        break
        return self.availableMoves
