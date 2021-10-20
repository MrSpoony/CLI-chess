class Rook:

    def __init__(self, xPos, yPos, color):
        self.char = "R"
        self.pos = [xPos, yPos]
        self.color = color

        # so you know which color it is, there is a "W" in front if it's a piece of white and the opposite with a "B" for black 
        if self.color:
            self.char = "W" + self.char
        else:
            self.char = "B" + self.char

        self.availableMoves = [self.char]
    
    def isAvailable(self, x, y, chessboard):
        if not(x <= -1 or y <= -1 or y >= len(chessboard) or x >= len(chessboard[0])):
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

    def setNewCoordinates(self, chessboard):
        for i in range(len(chessboard[int(self.color)])):
            for j in range(len(chessboard[int(self.color)][i])):
                if chessboard[int(self.color)][i][j] != " ":
                    if chessboard[int(self.color)][i][j].pos == self.pos:
                        self.pos = [j, i]

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