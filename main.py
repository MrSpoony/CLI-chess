from king import King
from queen import Queen
from bishop import Bishop
from knight import Knight
from pawn import Pawn
from rook import Rook

def createBoard():
    '''
    Creates a new clean Board

    '''
    chessboard = [[]] * (8)
    chessboard[0].append(" "*8)
    for j in range(len(chessboard)):
        for i in range(len(chessboard[j])):
            chessboard[j] = [char for char in chessboard[j][i]]

    for j in range(len(chessboard)):
        for i in range(len(chessboard[j])):
            pass
        
    return chessboard

def createWhiteSide():
    '''
    Creates the White Side of the chessboard with all its figures
    
    '''
    chessboard = createBoard()
    for i in range(len(chessboard[6])):
        chessboard[6][i] = Pawn(i, 6)

    chessboard[7][0] = Rook(0, 7)
    chessboard[7][1] = Knight(1, 7)
    chessboard[7][2] = Bishop(2, 7)
    chessboard[7][3] = Queen(3, 7)
    chessboard[7][4] = King(4, 7)
    chessboard[7][5] = Knight(5, 7)
    chessboard[7][6] = Bishop(6, 7)
    chessboard[7][7] = Rook(7, 7)
    return chessboard


def createBlackSide():
    '''
    Creates the Black Side of the chessboard with all its figures
    
    '''

    chessboard = createBoard()
    for i in range(len(chessboard[6])):
        chessboard[1][i] = Pawn(i, 6)
        
    chessboard[0][0] = Rook(0, 7)
    chessboard[0][1] = Knight(1, 7)
    chessboard[0][2] = Bishop(2, 7)
    chessboard[0][3] = King(3, 7)
    chessboard[0][4] = Queen(4, 7)
    chessboard[0][5] = Knight(5, 7)
    chessboard[0][6] = Bishop(6, 7)
    chessboard[0][7] = Rook(7, 7)
    return chessboard

