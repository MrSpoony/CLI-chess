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
