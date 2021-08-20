class Knight:

    def __init__(self, xPos, yPos, color):
        self.char = "N"
        self.pos = [xPos, yPos]
        self.color = color
        self.availableMoves = []

    def isAvailable(self, x, y, chessboard):
        if x != -1 and y != -1 and y != len(chessboard) and x != len(chessboard[0]):
            if chessboard[y][x] == " ":
                return True
            else:
                return False
        else:
            return False

    def isAvailableOpponent(self, x, y, chessboard):
        if chessboard[y][x] == " ":
            return True
        else:
            return False


    def checkForAvailableMoves(self, chessboard):
        moveOffsetOptionsY = [-1, 1]
        moveOffsetOptionsX = [-2, 2]
        for i in range(2):
            for i in range(len(moveOffsetOptionsY)):
                for j in range(len(moveOffsetOptionsX)):
                    while True:
                        if self.isAvailable(self.pos[0] + moveOffsetOptionsY[i], self.pos[1] + moveOffsetOptionsX[j], chessboard[int(self.color)]):
                            if self.isAvailableOpponent(self.pos[0] + moveOffsetOptionsY[i], self.pos[1] + moveOffsetOptionsX[j], chessboard[int(not self.color)]):
                                self.availableMoves.append([self.pos[0]  + moveOffsetOptionsY[i], self.pos[1] + moveOffsetOptionsX[j]])
                            else:
                                self.availableMoves.append([self.pos[0]  + moveOffsetOptionsY[i], self.pos[1] + moveOffsetOptionsX[j]])
                                break
                        else:
                            break
            moveOffsetOptionsX, moveOffsetOptionsY = moveOffsetOptionsY, moveOffsetOptionsX
        return self.availableMoves