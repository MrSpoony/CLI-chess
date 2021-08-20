from king import King
from queen import Queen
from bishop import Bishop
from knight import Knight
from pawn import Pawn
from rook import Rook


moveOfPlayer = True     # True if its the turn of white and False if its blacks turn, because white starts its True




def printBoard(chessboard):
    print("\n"*4)
    for i in range(len(chessboard)):
        print("\n", end="", flush=True)
        for j in range(len(chessboard[i])):
            if chessboard[i][j] != " ":
                print(chessboard[i][j].char, end="", flush=True)
            else:
                print(" ", end="", flush=True)




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
        chessboard[6][i] = Pawn(i, 6, True)

    chessboard[7][0] = Rook(0, 7, True)
    chessboard[7][1] = Knight(1, 7, True)
    chessboard[7][2] = Bishop(2, 7, True)
    chessboard[3][3] = Queen(3, 3, True)
    chessboard[7][4] = King(4, 7, True)
    chessboard[7][5] = Knight(5, 7, True)
    chessboard[7][6] = Bishop(6, 7, True)
    chessboard[7][7] = Rook(7, 7, True)
    return chessboard


def createBlackSide():
    '''
    Creates the Black Side of the chessboard with all its figures
    
    '''

    chessboard = createBoard()
    for i in range(len(chessboard[6])):
        chessboard[1][i] = Pawn(i, 6, False)
        
    chessboard[0][0] = Rook(0, 7, False)
    chessboard[0][1] = Knight(1, 7, False)
    chessboard[0][2] = Bishop(2, 7, False)
    chessboard[0][3] = King(3, 7, False)
    chessboard[0][4] = Queen(4, 7, False)
    chessboard[0][5] = Knight(5, 7, False)
    chessboard[0][6] = Bishop(6, 7, False)
    chessboard[0][7] = Rook(7, 7, False)
    return chessboard

def mergeBoards(chessboard):
    '''
    merges array of boards to one board and returns that
    
    '''
    newBoard = createBoard()
    for i in range(len(chessboard[0])):
        for j in range(len(chessboard[0][i])):
            if chessboard[0][i][j] != " ":
                newBoard[i][j] = chessboard[0][i][j]
            elif chessboard[1][i][j] != " ":
                newBoard[i][j] = chessboard[1][i][j]
    return newBoard

def isValidInput(userInput):
    '''
    checks if the userInput is a valid Input or not
    
    '''
    if len(userInput) != 4:
        return False
    if not(ord(userInput[0]) <= 104 and ord(userInput[0]) >= 97) or not(ord(userInput[2]) <= 104 and ord(userInput[2]) >= 97):
        return False
    if not(ord(userInput[1]) <= 56 or ord(userInput[1]) <= 49) or not(ord(userInput[3]) <= 56 or ord(userInput[3]) <= 49):
        return False
    return True

def convertInputToNumbers(userInput):
    '''
    converts the input to numbers
    
    '''
    numbers = []
    numbers.append(ord(userInput[0])-97)
    numbers.append(ord(userInput[1])-49)
    numbers.append(ord(userInput[2])-97)
    numbers.append(ord(userInput[3])-49)
    return numbers

def isFigureAtPosition(positions, wholeChessboard):
    '''
    checks if the position given is a piece on the chessboard from the right player
    
    '''
    if wholeChessboard[int(moveOfPlayer)][positions[1]][positions[0]] != " ":
        return True
    else:
        return False

whiteBoard = createWhiteSide()
blackBoard = createBlackSide()
chessboard = [blackBoard, whiteBoard]

printBoard(mergeBoards(chessboard))

print(chessboard[1][3][3].checkForAvailableMoves(chessboard))