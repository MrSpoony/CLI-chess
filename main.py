from heapq import merge
from pynvim import command
from King import King
from Queen import Queen
from Bishop import Bishop
from Knight import Knight
from Pawn import Pawn
from Rook import Rook
from copy import deepcopy

'''
coordinates Are always given in the Format [x, y]
But the Chess Array is made/printed in the Format whiteOrBlack, y, x 
So change the coordinates when interchanging them between pieces and Chess Arrays 
'''

def printBoard(chessboard):
    '''
    prints the chessboard that gets inputed
    
    '''
    print("\n"*4)
    for i in range(len(chessboard)):
        print(f"\n{9-(i+1)} ", end="|", flush=True)
        for j in range(len(chessboard[i])):
            if chessboard[i][j] != " ":
                print(str(chessboard[i][j]), end="|", flush=True)
            else:
                print("  ", end="|", flush=True)
            if len(chessboard)-1 == j:
                print("\n", end="", flush=True)
                print("  ", end="", flush=True)
                print("-"*(8*3+1), end="", flush=True)
    else:
        print("\n", end="", flush=True)
        print("   ", end="", flush=True)
        for i in range(len(chessboard)):
            print(chr((i+1) + 64), end="  ", flush=True)
        else:
            print("\n")

def printMoves(chessboard, whiteOrBlack):
    printBoard(mergeBoards(chessboard))
    print("Your possible moves are currently: ")
    possibleMoves = allPossibleMoves(chessboard, whiteOrBlack)
    for i in possibleMoves:
        if possibleMoves.index(i) != len(possibleMoves) - 1:
            print(i, end=", ", flush=True)
        else:
            print(i)
    print("\n")

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
    chessboard[7][3] = Queen(3, 7, True)
    chessboard[7][4] = King(4, 7, True)
    chessboard[7][5] = Bishop(5, 7, True)
    chessboard[7][6] = Knight(6, 7, True)
    chessboard[7][7] = Rook(7, 7, True)
    return chessboard

def createBlackSide():
    '''
    Creates the Black Side of the chessboard with all its figures
    
    '''

    chessboard = createBoard()
    for i in range(len(chessboard[6])):
        chessboard[1][i] = Pawn(i, 1, False)
        
    chessboard[0][0] = Rook(0, 0, False)
    chessboard[0][1] = Knight(1, 0, False)
    chessboard[0][2] = Bishop(2, 0, False)
    chessboard[0][3] = Queen(3, 0, False)
    chessboard[0][4] = King(4, 0, False)
    chessboard[0][5] = Bishop(5, 0, False)
    chessboard[0][6] = Knight(6, 0, False)
    chessboard[0][7] = Rook(7, 0, False)
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
    using unicode decodation
    
    '''
    if len(userInput) != 4:
        return False
    if not(ord(userInput[0]) <= 104 and ord(userInput[0]) >= 97) or not(ord(userInput[2]) <= 104 and ord(userInput[2]) >= 97):
        return False
    if not(ord(userInput[1]) <= 56 or ord(userInput[1]) <= 49) or not(ord(userInput[3]) <= 56 or ord(userInput[3]) <= 49):
        return False
    return True

def isPieceAtPos(positions, wholeChessboard):
    '''
    checks if the position given is a piece on the chessboard from the right player
    
    '''
    if wholeChessboard[int(moveOfPlayer)][positions[1]][positions[0]] != " ":
        return True
    else:
        return False

def getValidInput():
    '''
    Gets a valid Input of the player and returns that, first it checks if the input is a command 
    if yes it first executes that command and asks again until it gets a right input
    '''
    while True:
        userInput = input("Please enter your move in the format a1a2 or enter commands to show all the commands:\n")
        if userInput.lower() in listOfCommands:
            doCommands(listOfCommands.index(userInput))
        elif isValidInput(userInput):
            convertedInput = convertInputToNumbers(userInput)
            if isPieceAtPos(convertedInput[0], chessboard):
                if convertedInput in allMoves(chessboard, moveOfPlayer, True):
                    if convertedInput in allPossibleMoves(chessboard, moveOfPlayer, True):
                        break
                    else:
                        print("Move sets player in check, try again")
                else:
                    print("Move is not available/possible, try again")
            else:
                print("No piece at that position, try again")
        else:
            print("No valid input, try again")
    return convertedInput

def doCommands(commandIndex):
    '''
    CommandIndex is the index of the input in the variable listOfCommands
    '''
    if commandIndex == 0:
        print("\n\nCommands: \n\nmoves:\t\tShows all possible moves for active player.\nexit:\t\tExits the match.\nshow:\t\tShows the chessboard again.\n")
    elif 1 <= commandIndex <= 2:
        printMoves(chessboard, moveOfPlayer)
    elif 3 <= commandIndex <= 4:
        printBoard(mergeBoards(chessboard))
    elif commandIndex == 5:
        exit()
 
def convertInputToNumbers(userInput):
    '''
    converts the input to numbers/coordinates using unicode 
    '''
    numbers = []
    numbers.append(ord(userInput[0])-97)
    numbers.append(7 - (ord(userInput[1])-49))
    numbers.append(ord(userInput[2])-97)
    numbers.append(7 - (ord(userInput[3])-49))
    numbers = [numbers[i:i+2] for i in range(0, len(numbers), 2)]
    return numbers

def convertNumbersLikeInput(numbers):
    '''
    converts the numbers to input using unicode 
    '''
    chars = ""
    chars += chr(numbers[0][0]+97)
    chars += str(8 - numbers[0][1])
    chars += chr(numbers[1][0]+97)
    chars += str(8 - numbers[1][1])
    return chars

def movePiece(coordinatesFrom, coordinatesTo, chessboard):
    '''
    first checks which color is moving 
    and moves this piece from the coordinates coordinatesFrom 
    to the coordinatesTo on the same board 
    then setting the old coordinates to " " 
    and setting the coordinateTo on the other board to " "
    '''
    if chessboard[0][coordinatesFrom[1]][coordinatesFrom[0]] != " ":
        chessboard[0][coordinatesTo[1]][coordinatesTo[0]] = chessboard[0][coordinatesFrom[1]][coordinatesFrom[0]]
        chessboard[0][coordinatesFrom[1]][coordinatesFrom[0]] = " "
        chessboard[1][coordinatesTo[1]][coordinatesTo[0]] = " "
        chessboard[0][coordinatesTo[1]][coordinatesTo[0]].setNewCoordinates(chessboard)
    elif chessboard[1][coordinatesFrom[1]][coordinatesFrom[0]] != " ":
        chessboard[1][coordinatesTo[1]][coordinatesTo[0]] = chessboard[1][coordinatesFrom[1]][coordinatesFrom[0]]
        chessboard[1][coordinatesFrom[1]][coordinatesFrom[0]] = " "
        chessboard[0][coordinatesTo[1]][coordinatesTo[0]] = " "
        chessboard[1][coordinatesTo[1]][coordinatesTo[0]].setNewCoordinates(chessboard)
    else:
        raise("The piece you are trying to move does not exist")
    return(chessboard)

def allMoves(chessboard, whiteOrBlack, asNumbers = False, withStartPosition = True):
    '''
    Returns a list containing all the moves which are returned by all the pieces of the whiteOrBlack player. 
    chessboard: the current wholeChessboard
    whiteOrBlack: moves for which person
    asNumbers: should the output be in numbers or in the human readable format (e2e4)
    withStartPosition: should the output contain the Startposition of the pieces works only if asNumbers is True if asNumbers is False the start Positions will still be in the Output.
    '''
    moves = []
    for i in range(len(chessboard)):
        for j in range(len(chessboard[i])):
            for k in range(len(chessboard[i][j])):
                if chessboard[i][j][k] != " ":
                    for l in range(len(chessboard[i][j][k].checkForAvailableMoves(chessboard))):
                        if chessboard[i][j][k].color == whiteOrBlack:
                            if asNumbers:
                                moves.append(chessboard[i][j][k].checkForAvailableMoves(chessboard)[l])
                            else:
                                moves.append(convertNumbersLikeInput(chessboard[i][j][k].checkForAvailableMoves(chessboard)[l]))
    if (not withStartPosition) and asNumbers:
        removesStartPosition(moves)
    return moves

def allPossibleMoves(chessboard, whiteOrBlack, asNumbers = False, withStartPosition = True):
    '''
    Returns all moves that are currently possible, excluding the ones which set the king into check
    '''
    moves = allMoves(chessboard, whiteOrBlack, True, True)
    possibleMoves = []
    for move in moves:
        staticChessboard = deepcopy(chessboard)
        tempChessboard = movePiece(move[0], move[1], staticChessboard)
        if not isCheck(tempChessboard, whiteOrBlack):
            if asNumbers:
                possibleMoves.append(move)
            else:
                possibleMoves.append(convertNumbersLikeInput(move))
        resetAllCoordinates(chessboard)
    if (not withStartPosition) and asNumbers:
        removesStartPosition(possibleMoves)
    return possibleMoves

def resetAllCoordinates(chessboard):
    '''
    Resets all Coordinates of the pieces which are on the board, so if they got changed, they will be reset here
    
    '''
    for i in range(len(chessboard)):
        for j in range(len(chessboard[i])):
            for k in range(len(chessboard[i][j])):
                if chessboard[i][j][k] != " ":
                    chessboard[i][j][k].setNewCoordinates(chessboard)
    return chessboard

def removesStartPosition(moves):
    '''
    removes the first half of each item in the array so there are only the endpositions
    example:    [[[0, 0], [1, 1]], [[1, 1], [2, 2]]]
    to:         [[1, 1], [2, 2]]
    '''
    for i in range(len(moves)):
        moves[i] = moves[i][1]

def isCheck(chessboard, whiteOrBlack):
    '''
    checks if the whiteOrBlack player is in check in the board chessboard
    returns True or False
    '''
    moves = allMoves(chessboard, not whiteOrBlack, True, False)
    for i in range(len(chessboard[int(whiteOrBlack)])):
        for j in range(len(chessboard[int(whiteOrBlack)][i])):
            if str(chessboard[int(whiteOrBlack)][i][j]) in {"WK", "BK"}:
                posKing = [j, i]
    movesWithoutDuplicates = []
    for move in moves:
        if move not in movesWithoutDuplicates:
            movesWithoutDuplicates.append(move)
    moves = movesWithoutDuplicates
    for move in moves:
        if move == posKing:
            return True
    return False

def checkForCheckmate(chessboard, whiteOrBlack):
    '''
    checks if the whiteOrBlack player's king is checkmated, returns True or False
    
    '''
    for i in range(len(chessboard[int(whiteOrBlack)])):
        for j in range(len(chessboard[int(whiteOrBlack)][i])):
            if "K" in chessboard[int(whiteOrBlack)][i][j]:
                king = chessboard[int(whiteOrBlack)][i][j]
    movesPossibleOpponent = allMoves(chessboard, not whiteOrBlack, True, False)
    possibleMovesKing = king.checkforAvailableMoves(chessboard)
    for i in possibleMovesKing:
        if i in movesPossibleOpponent:
            possibleMovesKing.remove(i)
    if possibleMovesKing != [] and king.pos in movesPossibleOpponent:
        return False
    else:
        return True



moveOfPlayer = True     # True if its the turn of white and False if its blacks turn, because white starts its set to True
listOfCommands = ["commands", "moves", "turns", "show", "showboard", "exit", "quit"]

# Create the two boards and merge them
whiteBoard = createWhiteSide()
blackBoard = createBlackSide()
chessboard = [blackBoard, whiteBoard]

# print first board
printBoard(mergeBoards(chessboard))

while True:
    playerMove = getValidInput()
    chessboard = movePiece(playerMove[0], playerMove[1], chessboard)
    printBoard(mergeBoards(chessboard))
    moveOfPlayer = not moveOfPlayer