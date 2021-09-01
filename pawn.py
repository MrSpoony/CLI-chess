class Pawn:

    def __init__(self, xPos, yPos, color):
        self.char = "P"
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
        if self.isAvailable(self.pos[0], self.pos[1] - 1, chessboard[int(self.color)]):
            if self.isAvailableOpponent(self.pos[0], self.pos[1] - 1, chessboard[int(not self.color)]):
                self.availableMoves.append([self.pos[0], self.pos[1] - 1])
        for i in range(-1, 2, 2):
            if self.isAvailable(self.pos[0] + i, self.pos[1] - 1, chessboard[int(self.color)]):
                if not self.isAvailableOpponent(self.pos[0] + i, self.pos[1] - 1, chessboard[int(not self.color)]):
                    self.availableMoves.append([self.pos[0] + i, self.pos[1] - 1])
        return self.availableMoves