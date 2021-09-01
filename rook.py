class Rook:

    def __init__(self, xPos, yPos, color):
        self.char = "R"
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
        moveOffsetOptions = [-1, 0, 1]
        for i in range(len(moveOffsetOptions)):
            for j in range(len(moveOffsetOptions)):
                currentOffsetX = moveOffsetOptions[i]
                currentOffsetY = moveOffsetOptions[j]
                if not(currentOffsetY == 0 or currentOffsetX == 0):
                    continue
                steps = 1
                while True:
                    if self.isAvailable(self.pos[0] + currentOffsetX, self.pos[1] + currentOffsetY, chessboard[int(self.color)]):
                        if self.isAvailableOpponent(self.pos[0] + currentOffsetX, self.pos[1] + currentOffsetY, chessboard[int(not self.color)]):
                            self.availableMoves.append([self.pos[0]  + currentOffsetX, self.pos[1] + currentOffsetY])
                            steps += 1
                        else:
                            self.availableMoves.append([self.pos[0]  + currentOffsetX, self.pos[1] + currentOffsetY])
                            steps += 1
                            break
                        currentOffsetX = moveOffsetOptions[i]*steps
                        currentOffsetY = moveOffsetOptions[j]*steps
                    else:
                        break
        return self.availableMoves