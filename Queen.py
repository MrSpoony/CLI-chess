from Piece import Piece
class Queen(Piece):

    def __init__(self, xPos, yPos, color):
        super().__init__(xPos, yPos, color)
        self.char += "Q"

    def checkForAvailableMoves(self, chessboard):
        moveOffsetOptions = [-1, 0, 1]
        for i in range(len(moveOffsetOptions)):
            for j in range(len(moveOffsetOptions)):
                currentOffsetX = moveOffsetOptions[i]
                currentOffsetY = moveOffsetOptions[j]
                steps = 1
                while True:
                    if self.isAvailable(self.pos[0] + currentOffsetX, self.pos[1] + currentOffsetY, chessboard[int(self.color)]):
                        if self.isAvailableOpponent(self.pos[0] + currentOffsetX, self.pos[1] + currentOffsetY, chessboard[int(not self.color)]):
                            self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0]  + currentOffsetX, self.pos[1] + currentOffsetY]])
                            steps += 1
                        else:
                            self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0]  + currentOffsetX, self.pos[1] + currentOffsetY]])
                            steps += 1
                            break
                        currentOffsetX = moveOffsetOptions[i]*steps
                        currentOffsetY = moveOffsetOptions[j]*steps
                    else:
                        break
        return self.availableMoves