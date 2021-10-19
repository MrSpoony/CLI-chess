class Pawn:

    def __init__(self, xPos, yPos, color):
        self.char = "P"
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


    def checkForAvailableMoves(self, chessboard):
        if self.isAvailable(self.pos[0], self.pos[1] - 1, chessboard[int(self.color)]):
            if self.isAvailableOpponent(self.pos[0], self.pos[1] - 1, chessboard[int(not self.color)]):
                self.availableMoves.append([self.pos[0], self.pos[1] - 1])
        for i in range(-1, 2, 2):
            if self.isAvailable(self.pos[0] + i, self.pos[1] - 1, chessboard[int(self.color)]):
                if not self.isAvailableOpponent(self.pos[0] + i, self.pos[1] - 1, chessboard[int(not self.color)]):
                    self.availableMoves.append([self.pos[0] + i, self.pos[1] - 1])
        return self.availableMoves