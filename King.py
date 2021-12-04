from Piece import Piece
from Rook import Rook
import colorama
class King(Piece):

    def __init__(self, xPos, yPos, color):
        '''
        New King Piece at position xPos, yPos, and the color color'''
        super().__init__(xPos, yPos, color)
        self.char += "K" + colorama.Style.RESET_ALL

    def __str__(self):
        '''
        Sets the Sring of the Object to it's char so I can access it with str()'''
        return self.char

    def checkForAvailableMoves(self, chessboard):
        '''
        Checks for the available moves from this piece'''
        self.availableMoves = []
        moveOffsetOptions = [-1, 0, 1]
        for i in range(len(moveOffsetOptions)):
            for j in range(len(moveOffsetOptions)):
                currentOffsetX = moveOffsetOptions[i]
                currentOffsetY = moveOffsetOptions[j]
                if self.isAvailable(self.pos[0] + currentOffsetX, self.pos[1] + currentOffsetY, chessboard[int(self.color)]):
                    self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0]  + currentOffsetX, self.pos[1] + currentOffsetY]])
        self.checkForRochade(chessboard)
        return self.availableMoves

    def checkForRochade(self, chessboard):
        '''
        Checks if there is a rochade possible/available
        if yes then it appends the rochade moves to self.availableMoves'''
        if not self.moved:
            if self.color:
                if type(chessboard[int(self.color)][7][0]) is Rook:
                    if not chessboard[int(self.color)][7][0].moved:
                        if chessboard[int(self.color)][7][1] == " " and chessboard[int(self.color)][7][2] == " " and chessboard[int(self.color)][7][3] == " ":
                            if chessboard[int(not self.color)][7][1] == " " and chessboard[int(not self.color)][7][2] == " " and chessboard[int(not self.color)][7][3] == " ":
                                self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0] - 2, self.pos[1]]])
                if type(chessboard[int(self.color)][7][7]) is Rook:
                    if not chessboard[int(self.color)][7][7].moved:
                        if chessboard[int(self.color)][7][6] == " " and chessboard[int(self.color)][7][5] == " ":
                            if chessboard[int(not self.color)][7][6] == " " and chessboard[int(not self.color)][7][5]:
                                self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0] + 2, self.pos[1]]])
            else:
                if type(chessboard[int(self.color)][0][0]) is Rook:
                    if not chessboard[int(self.color)][0][0].moved:
                        if chessboard[int(self.color)][0][1] == " " and chessboard[int(self.color)][0][2] == " " and chessboard[int(self.color)][0][3] == " ":
                            if chessboard[int(not self.color)][0][1] == " " and chessboard[int(not self.color)][0][2] == " " and chessboard[int(not self.color)][0][3] == " ":
                                self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0] - 2, self.pos[1]]])
                if type(chessboard[int(self.color)][0][7]) is Rook:
                    if not chessboard[int(self.color)][0][7].moved:
                        if chessboard[int(self.color)][0][6] == " " and chessboard[int(self.color)][0][5] == " ":
                            if chessboard[int(not self.color)][0][6] == " " and chessboard[int(not self.color)][0][5]:
                                self.availableMoves.append([[self.pos[0], self.pos[1]], [self.pos[0] + 2, self.pos[1]]])
