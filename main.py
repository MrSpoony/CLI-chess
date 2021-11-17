from colorama.ansi import Fore
from King import King
from Queen import Queen
from Bishop import Bishop
from Knight import Knight
from Pawn import Pawn
from Rook import Rook
from copy import deepcopy
import colorama

# Import all the pieces
# To copy without problems import copy (deepcopy)
# For nice colors import colorama



# Short explenation of the further code

# The chessboards are always a 3D array, [which color to look for][y coordinate][x coordinate]
# I seperated the white and black side, because it is easier for the overview and, also easier to look for the pieces you need/don't need
# If you want to have just one board merge them with the mergeBoards(chessboard) function, with which you can merge them into one board

# Coordinates on the other hand are always given in the Format [x, y]
# So change the coordinates when interchanging them between pieces and Chess Arrays 




moveOfPlayer = True  # True if its the turn of white and False if its blacks turn, because white starts its set to True
listOfCommands = [   # list which includes all commands so that expanding is easier later each [i] is a further array with all the commands which have the same purpose 
["commands", "command", "help", "--help", "man", "?"], 
["moves", "possiblemoves", "turns", "possibleturns", "listmoves", "printmoves", "showmoves", "list", "lsmoves", "ls", "ll"], 
["show", "showboard", "board", "chessboard", "printboard"], 
["exit", "quit", ":wq", "leave", ":q", "q"], 
["clear", "cls", "c"]] 


def printBoard(chessboard):
    '''
    Prints the chessboard that gets inputed and adds the seperators and the ABC and 123 indicators
    '''
    print("\n"*4)

    print("   ", end="", flush=True)
    for i in range(len(chessboard)):
        print(chr((i+1) + 64), end="  ", flush=True)

    print()
    print("  ", end="", flush=True)
    print("-"*(8*3+1), end="", flush=True)

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
    '''
    Printes all the moves under a fresh printed chessboard
    '''
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
    Creates a new clean Board, but only a 2D one not a 3D one
    '''
    # Create empty 1x8 board
    chessboard = [[]] * (8)
    # Add 8 spaces to the first element
    chessboard[0].append(" "*8)
    for j in range(len(chessboard)):
        for i in range(len(chessboard[j])):
            chessboard[j] = [char for char in chessboard[j][i]]

    return chessboard

def createWhiteSide():
    '''
    Creates the White Side of the chessboard with all its figures
    '''
    # Create all the white pawns
    chessboard = createBoard()
    for i in range(len(chessboard[6])):
        chessboard[6][i] = Pawn(i, 6, True)

    #Create all the other white pieces
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
    # Create all the black pawns 
    chessboard = createBoard()
    for i in range(len(chessboard[6])):
        chessboard[1][i] = Pawn(i, 1, False)

    # Create all the other black pieces 
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
    Merges array of boards to one board and returns that
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
    Checks if the userInput is a valid Input or not (only checks if the input is 4 characters long and if the input is within the bounds of A-H and 1-8) 
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
    Checks if the position given is a piece on the chessboard from the right player
    '''
    if wholeChessboard[int(moveOfPlayer)][positions[1]][positions[0]] != " ":
        return True
    else:
        return False

def doCommands(input, getIndex = False):
    '''
    Executes the given Input, if getIndex is True, it returns the index of the command in the array listOfCommands
    If the input is not a command, it returns 2**31 (almost max integer limit) so that the program knows that there is no valid command to execute
    '''
    index = 2**31
    for i in range(len(listOfCommands)):
        if input in listOfCommands[i]:
            index = i
    if getIndex:
        return index
    else:
        if index == 0:
            showCommands() 
        elif index == 1:
            printMoves(chessboard, moveOfPlayer)
        elif index == 2:
            printBoard(mergeBoards(chessboard))
        elif index == 3:
            exit()
        elif index == 4:
            print("\n"*100)

def getValidInput(moves):
    '''
    Gets a valid Input of the player and returns that, first it checks if the input is a command 
    if yes it first executes that command and asks again until it gets a right input
    Includes the functions isPieceAtPos() and isValidInput(), for the commands is uses the function doCommands()
    Returns the valid input convertet to numbers in the form [[x, y], [x, y]] 
    '''
    while True:
        if moveOfPlayer:
            print("Whites turn: ")
        else:
            print("Blacks turn: ")
        userInput = input("Please enter your move in the format a1a2 or enter commands to show all the commands:\n")
        if doCommands(userInput.lower(), True) != 2**31:
            doCommands(userInput.lower())
        elif isValidInput(userInput):
            convertedInput = convertInputToNumbers(userInput)
            if isPieceAtPos(convertedInput[0], chessboard):
                if convertedInput in allMoves(chessboard, moveOfPlayer, True):
                    possibleMoves = moves
                    if convertedInput in possibleMoves:
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

def showCommands():
    '''
    Shows all available commands including a little description of what they do
    '''
    print("\n\n\n\n\n\nCommands:\n\n")
    for i in range(len(listOfCommands)):
        for j in range(len(listOfCommands[i])):
            print(listOfCommands[i][j], end="", flush=True)
            if j == 0:
                if i == 0:
                    print("\t\tPrints this table again. ")
                elif i == 1:
                    print("\t\t\tShows all moves for the current active player. ")
                elif i == 2:
                    print("\t\t\tExits the program, DOES QUIT YOUR MATCH! ")
                elif i == 3:
                    print("\t\t\tShows the current chessboard again. ")
            elif j == len(listOfCommands[i])-1:
                print("\n")
            else:
                print() 

def convertInputToNumbers(userInput):
    '''
    Converts the userInput to numbers/coordinates using unicode 
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
    Converts the numbers to input using unicode 
    '''
    chars = ""
    chars += chr(numbers[0][0]+97)
    chars += str(8 - numbers[0][1])
    chars += chr(numbers[1][0]+97)
    chars += str(8 - numbers[1][1])
    return chars

def movePiece(coordinatesFrom, coordinatesTo, chessboard):
    '''
    First checks which color is moving 
    and moves this piece from the coordinates coordinatesFrom 
    to the coordinatesTo on the same board 
    then setting the old coordinates to " " 
    and setting the coordinateTo on the other board to " ", so that the other piece get deleted
    '''
    if chessboard[0][coordinatesFrom[1]][coordinatesFrom[0]] != " ":
        chessboard[0][coordinatesTo[1]][coordinatesTo[0]] = chessboard[0][coordinatesFrom[1]][coordinatesFrom[0]]
        chessboard[0][coordinatesTo[1]][coordinatesTo[0]].moved = True
        chessboard[0][coordinatesFrom[1]][coordinatesFrom[0]] = " "
        chessboard[1][coordinatesTo[1]][coordinatesTo[0]] = " "
        chessboard[0][coordinatesTo[1]][coordinatesTo[0]].setNewCoordinates(chessboard)
    elif chessboard[1][coordinatesFrom[1]][coordinatesFrom[0]] != " ":
        chessboard[1][coordinatesTo[1]][coordinatesTo[0]] = chessboard[1][coordinatesFrom[1]][coordinatesFrom[0]]
        chessboard[1][coordinatesTo[1]][coordinatesTo[0]].moved = True
        chessboard[1][coordinatesFrom[1]][coordinatesFrom[0]] = " "
        chessboard[0][coordinatesTo[1]][coordinatesTo[0]] = " "
        chessboard[1][coordinatesTo[1]][coordinatesTo[0]].setNewCoordinates(chessboard)
    else:
        raise("The piece you are trying to move does not exist\nThis should never be executed or my getValidInput method does something wrong")
    return(chessboard)

def isTurnRochade(chessboard, whiteOrBlack, possibleMoves):
    for i in possibleMoves:
        if [[],[]]:
            pass

def allMoves(chessboard, whiteOrBlack, asNumbers = False, withStartPosition = True):
    '''
    Returns a list containing all the moves which are returned by all the pieces of the whiteOrBlack player. 
    chessboard: the current wholeChessboard
    whiteOrBlack: moves for which person
    asNumbers: should the output be in numbers or in the human readable format (e2e4)
    withStartPosition: should the output contain the Startposition of the pieces works only if asNumbers is True if asNumbers is False the start Positions will still be in the Output.
    '''
    moves = []

    for i in range(len(chessboard[int(whiteOrBlack)])):
        for j in range(len(chessboard[int(whiteOrBlack)][i])):
            if chessboard[int(whiteOrBlack)][i][j] != " ":
                avalableMovesCurrentPiece = chessboard[int(whiteOrBlack)][i][j].checkForAvailableMoves(chessboard)
                for k in range(len(avalableMovesCurrentPiece)):
                    if asNumbers:
                        moves.append(avalableMovesCurrentPiece[k])
                    else:
                        moves.append(convertNumbersLikeInput(avalableMovesCurrentPiece[k]))
    if (not withStartPosition) and asNumbers:
        removesStartPosition(moves)
    return moves

def allPossibleMoves(chessboard, whiteOrBlack, asNumbers = False, withStartPosition = True):
    '''
    Returns all moves that are currently possible, excluding the ones which set the king into check
    chessboard: the current wholeChessboard
    whiteOrBlack: moves for which person
    asNumbers: should the output be in numbers or in the human readable format (e2e4)
    withStartPosition: should the output contain the Startposition of the pieces works only if asNumbers is True if asNumbers is False the start Positions will still be in the Output.
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
    example:
    from        [[[0, 0], [1, 1]], [[1, 1], [2, 2]]]
    to:         [[1, 1], [2, 2]]
    '''
    for i in range(len(moves)):
        moves[i] = moves[i][1]

def isCheck(chessboard, whiteOrBlack):
    '''
    Checks if the whiteOrBlack player is in check on the board chessboard
    returns True or False
    '''
    moves = allMoves(chessboard, not whiteOrBlack, True, False)
    for i in range(len(chessboard[int(whiteOrBlack)])):
        for j in range(len(chessboard[int(whiteOrBlack)][i])):
            if type(chessboard[int(whiteOrBlack)][i][j]) is King:
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

def isCheckMate(moves):
    '''
    Checks if there are any possible moves, if not, the player is checkmated
    returns True or False
    '''
    if moves == []: 
        return True
    else:
        return False

def checkIfPawnAtEnd(chessboard, whiteOrBlack):
    '''
    Checks if a pawn is at the end of the board, if this is the case
    this pawn gets replaced with a new piece chosen by the current player'''
    if whiteOrBlack:
        for i in range(len(chessboard[int(whiteOrBlack)][7])):
            if colorama.Fore.BLUE + "WP" + colorama.Style.RESET_ALL in str(chessboard[int(whiteOrBlack)][0][i]):
                chessboard[int(whiteOrBlack)][0][i] = " "
                chessboard[int(whiteOrBlack)][0][i] = getValidInputForNewEndPiece()(i, 0, True)
    else:
        for i in range(len(chessboard[int(whiteOrBlack)][7])):
            if colorama.Fore.BLUE + "WP" + colorama.Style.RESET_ALL in str(chessboard[int(whiteOrBlack)][7][i]):
                chessboard[int(whiteOrBlack)][7][i] = " "
                chessboard[int(whiteOrBlack)][7][i] = getValidInputForNewEndPiece()(i, 7, True)

def getValidInputForNewEndPiece():
    '''
    Gets a valid input for the checkIfPawnAtEnd method
    returns a piece object wich then can be reused to initiate the new piece'''
    print("Your pawn got to the end, you can choose a piece now:")
    print("Which piece do you want? ")
    print("[Q]ueen, k[N]ight, [B]ishop, [R]ook")
    while True:
        userInput = input().lower()
        if userInput == "q" or userInput == "queen":
            return Queen
        elif userInput == "n" or userInput == "knight":
            return Knight
        elif userInput == "b" or userInput == "bishop":
            return Bishop
        elif userInput == "r" or userInput == "rook":
            return Rook
        else:
            print("No valid piece, try again")

def gameOver():
    '''
    Prints the Game Over statement and exits the program
    '''
    if moveOfPlayer:
        print("GameOver\nBlack won! GG")
    else:
        print("GameOver\nWhite won! GG")
    exit()

# Create the two boards and merge them
whiteBoard = createWhiteSide()
blackBoard = createBlackSide()
chessboard = [blackBoard, whiteBoard]

# print first board
printBoard(mergeBoards(chessboard))

while True:
    '''
    Main loop which gets called every turn
    '''
    possibleMoves = allPossibleMoves(chessboard, moveOfPlayer, True)
    if isCheckMate(possibleMoves):
        gameOver()
    playersMove = getValidInput(possibleMoves)
    chessboard = movePiece(playersMove[0], playersMove[1], chessboard)
    checkIfPawnAtEnd(chessboard, moveOfPlayer)
    printBoard(mergeBoards(chessboard))
    moveOfPlayer = not moveOfPlayer