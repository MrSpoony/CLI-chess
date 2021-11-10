from Piece import Piece
import colorama
class King(Piece):

    def __init__(self, xPos, yPos, color):
        super().__init__(xPos, yPos, color)
        self.char += "K" + colorama.Style.RESET_ALL

    def __str__(self):
        return self.char
        
    def checkForAvailableMoves(self, chessboard):
        self.availableMoves = []
        moveOffsetOptions = [-1, 0, 1]
        for i in range(len(moveOffsetOptions)):
            for j in range(len(moveOffsetOptions)):
                currentOffsetX = moveOffsetOptions[i]
                currentOffsetY = moveOffsetOptions[j]
                if self.isAvailable(self.pos[0] + currentOffsetX, self.pos[1] + currentOffsetY, chessboard[int(self.color)]):
                    self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0]  + currentOffsetX, self.pos[1] + currentOffsetY]])
        return self.availableMoves