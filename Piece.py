import colorama
class Piece:

    def __init__(self, xPos, yPos, color):
        self.pos = [xPos, yPos]
        self.color = color
        self.availableMoves = []
        # so you know which color it is, there is a "W" in front if it's a piece of white and the opposite with a "B" for black 
        if self.color:
            self.char = colorama.Fore.BLUE + "W"
        else:
            self.char = colorama.Fore.RED + "B"

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