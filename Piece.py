import colorama
class Piece:

    def __init__(self, xPos, yPos, color):
        self.pos = [xPos, yPos]
        self.color = color
        self.availableMoves = []
        self.moved = False
        # so you know which color it is, there is a blue "W" in front if it's a piece of white and the opposite with a red "B" for black 
        if self.color:
            self.char = colorama.Fore.BLUE + "W"
        else:
            self.char = colorama.Fore.RED + "B"

    def isAvailable(self, x, y, chessboard):
        '''
        Checks if position x, y on the chessboard of your own color is available'''
        if not(x <= -1 or y <= -1 or y >= len(chessboard) or x >= len(chessboard[0])):
            if chessboard[y][x] == " ":
                return True
            else:
                return False
        else:
            return False
            
    def setNewCoordinates(self, chessboard):
        '''
        Resets all the coordinates
        Loops through every piece checks it's position and writes that position to its self.pos variable'''
        for i in range(len(chessboard[int(self.color)])):
            for j in range(len(chessboard[int(self.color)][i])):
                if chessboard[int(self.color)][i][j] != " ":
                    if chessboard[int(self.color)][i][j].pos == self.pos:
                        self.pos = [j, i]