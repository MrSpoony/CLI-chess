#!/usr/bin/env python
from King import King
from Queen import Queen
from Bishop import Bishop
from Knight import Knight
from Pawn import Pawn
from Rook import Rook
from copy import deepcopy
from os import system, name
import colorama

# Import all the pieces
# To copy without problems import copy.deepcopy
# To clear the commandline import os.system
# To know which system you're on import os.name
# For nice colors import colorama



# Short explenation of the further code

# The chessboards are always a 3D array chessboard[which color to look for][y coordinate][x coordinate]
# I seperated the white and black side,
# because it is easier for the overview and
# also easier to look for the pieces you need / don't need
# If you want to have just one board merge them with the mergeBoards(chessboard) function,
# with which you can merge them into one board

#Coordinates on the other hand are always given in the Format[x, y]
# So change the coordinates when interchanging them between pieces and Chess / Arrays 




moveOfPlayer = True  # True if its the turn of white and False if its blacks turn, because white starts its set to True
listOfCommands = [   # list which includes all commands so that expanding is easier later each [i] is a further array with all the commands which have the same purpose 
    ["commands", "command", "help", "--help", "man", "?"],
    ["moves", "move", "possiblemoves", "turns", "possibleturns", "listmoves", "printmoves", "showmoves", "list", "lsmoves", "ls", "ll"],
    ["show", "showboard", "board", "chessboard", "printboard"],
    ["undo", "revoke"],
    ["remis", "draw"],
    ["exit", "quit", ":wq", "leave", ":q", "q"],
    ["clear", "cls", "c"]]

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def printBoard(chessboard):
    '''
    Clears the commandline,
    prints the chessboard that gets inputed and adds the seperators and the ABC and 123 indicators
    '''

    clear()
    print("\n")

    # Print the ABCD... at the top
    print("      ", end="", flush=True)
    for i in range(len(chessboard)):
        print(chr((i+1) + 64), end="  ", flush=True)

    # Print a line conisting of -------
    print()
    print("     ", end="", flush=True)
    print("-"*(8*3+1), end="", flush=True)

    for i in range(len(chessboard)):
        # Print number on the left side
        print(f"\n   {9-(i+1)} ", end="|", flush=True)
        for j in range(len(chessboard[i])):
            if chessboard[i][j] != " ":
                # Print the piece itself
                print(str(chessboard[i][j]), end="|", flush=True)
            else:
                # Or two spaces if there is no piece
                print("  ", end="|", flush=True)
            if len(chessboard)-1 == j:
                # Print a line conisting of -------
                print()
                print("     ", end="", flush=True)
                print("-"*(8*3+1), end="", flush=True)
                # print("\n", end="", flush=True)
                # print("  ", end="", flush=True)
                # print("-"*(8*3+1), end="", flush=True)

    else:
        # Print the ABCD... at the bottom
        print("\n", end="", flush=True)
        print("      ", end="", flush=True)
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

    # Create all the other white pieces
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
            undoMoves(1)
        elif index == 4:
            askForRemis()
            pass
        elif index == 5:
            exit()
        elif index == 6:
            clear()

def getValidInput(moves):
    '''
    Gets a valid Input of the player and returns that, first it checks if the input is a command 
    if yes it first executes that command and asks again until it gets a right input
    Includes the functions isPieceAtPos() and isValidInput(), for the commands is uses the function doCommands()
    Returns the valid input convertet to numbers in the form [[x, y], [x, y]] 
    '''
    # Whyever my code does not work if don't use the moves variable so I added a simple request to shut that warning
    if moves:
        pass

    while True:
        if moveOfPlayer:
            print("Whites turn: ")
        else:
            print("Blacks turn: ")
        userInput = input("Please enter your move in the format a1a2 or enter commands to show all the commands:\n")
        if doCommands(userInput.lower(), True) != 2**31:
            # If the undo command is executed update the moves
            if doCommands(userInput.lower(), True) == 3:
                # Whyever I need to use this line to privent me from getting a ton of warnings
                moves = allPossibleMoves(chessboard, moveOfPlayer, True)
            doCommands(userInput.lower())
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

def showCommands():
    '''
    Shows all available commands including a little description of what they do
    '''
    clear()
    print("Commands:\n")
    for i in range(len(listOfCommands)):
        for j in range(len(listOfCommands[i])):
            if j != 0:
                print("  ", end="", flush=True)
            print(listOfCommands[i][j], end="", flush=True)
            if j == 0:
                if i == 0:
                    print("\t\tPrints this table again. ")
                elif i == 1:
                    print("\t\t\tShows all moves for the current active player. ")
                elif i == 2:
                    print("\t\t\tExits the program, THIS QUITS YOUR MATCH WITHOUT ASKING AGAIN! ")
                elif i == 3:
                    print("\t\t\tUndos the last move made. ")
                elif i == 4:
                    print("\t\t\tAsks you and the player you're playing against to agree on a draw. ")
                elif i == 5:
                    print("\t\t\tShows the current chessboard again. ")
                elif i == 6:
                    print("\t\t\tClears the commandline. ")
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

def swapPieces(chessboard, whiteOrBlack, fromX, fromY, toX, toY):
    '''
    Swaps two pieces,
    first sets the moved variable of the piece to True
    then it moves the pieces,
    sets the "old" Piece to " ",
    sets the "new" position on the other board to " " and
    sets the new coordinates of the piece'''
    chessboard[whiteOrBlack][fromY][fromX].moved = True
    chessboard[whiteOrBlack][toY][toX] = chessboard[whiteOrBlack][fromY][fromX]
    chessboard[whiteOrBlack][fromY][fromX] = " "
    chessboard[int(not bool(whiteOrBlack))][toY][toX] = " "
    chessboard[whiteOrBlack][toY][toX].setNewCoordinates(chessboard)
    return chessboard

def movePiece(coordinatesFrom, coordinatesTo, chessboard):
    '''
    First checks if the Move is a rochade
    if yes it moves the King to it's new position, then the rook
    if no it checks which piece is moving and moves it
    '''
    # Check on both sides if the move is a rochade
    rochade = isTurnRochade(chessboard, False, coordinatesFrom, coordinatesTo)
    if not rochade:
        rochade = isTurnRochade(chessboard, True, coordinatesFrom, coordinatesTo)

    if rochade:
        # King to new pos
        chessboard = swapPieces(chessboard, rochade[0], coordinatesFrom[0], coordinatesFrom[1], coordinatesTo[0], coordinatesTo[1])
        # Rook to new pos
        if rochade[1]:
            if rochade[0]:
                chessboard = swapPieces(chessboard, 1, 0, 7, 3, 7)
            else:
                chessboard = swapPieces(chessboard, 0, 0, 0, 3, 0)
        else:
            if rochade[0]:
                chessboard = swapPieces(chessboard, 1, 7, 7, 5, 7)
            else:
                chessboard = swapPieces(chessboard, 0, 0, 7, 5, 0)
    else:
        if chessboard[0][coordinatesFrom[1]][coordinatesFrom[0]] != " ":
            chessboard = swapPieces(chessboard, 0, coordinatesFrom[0], coordinatesFrom[1], coordinatesTo[0], coordinatesTo[1])
        elif chessboard[1][coordinatesFrom[1]][coordinatesFrom[0]] != " ":
            chessboard = swapPieces(chessboard, 1, coordinatesFrom[0], coordinatesFrom[1], coordinatesTo[0], coordinatesTo[1])
        else:
            print("The piece you are trying to move does not exist\nThis should never be executed or my getValidInput method does something wrong")
            exit()
    return(chessboard)

def isTurnRochade(chessboard, whiteOrBlack, coordinatesFrom, coordinatesTo):
    '''
    Checks if the current move is a Rochade
    returns False if not, otherwise returns a list of [colorOfRochadeMove, isToTheLeft]
    when isToTheLeftIs 0 if the rochade is to the right
    if the rochade is to the left isToTheLeft is 1'''
    if whiteOrBlack:
        if type(chessboard[1][coordinatesFrom[1]][coordinatesFrom[0]]) is King:
            if coordinatesTo[0] == coordinatesFrom[0]+2:
                return [1, 0]
            elif coordinatesTo[0] == coordinatesFrom[0]-2:
                return [1, 1]
    else:
        if type(chessboard[0][coordinatesFrom[1]][coordinatesFrom[0]]) is King:
            if coordinatesTo[0] == coordinatesFrom[0]+2:
               return [0, 0]
            elif coordinatesTo[0] == coordinatesFrom[0]-2:
                return [0, 1]
    return False

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
    whiteOrBlack: moves for which person asNumbers: should the output be in numbers or in the human readable format (e2e4) withStartPosition: should the output contain the Startposition of the pieces works only if asNumbers is True if asNumbers is False the start Positions will still be in the Output.
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

def checkIfPawnAtEnd(goingThroughHistory = False):
    '''
    Checks if a pawn is at the end of the board, if this is the case
    this pawn gets replaced with a new piece chosen by the current player'''
    global chessboard
    global history
    global historyPawnIndex
    if not goingThroughHistory:
        if moveOfPlayer:
            for i in range(len(chessboard[1][0])):
                if colorama.Fore.BLUE + "WP" + colorama.Style.RESET_ALL in str(chessboard[1][0][i]):
                    newPieceInsteadOfPawn(True, i, 0)
        else:
            for i in range(len(chessboard[0][7])):
                if colorama.Fore.RED + "BP" + colorama.Style.RESET_ALL in str(chessboard[0][7][i]):
                    newPieceInsteadOfPawn(False, i, 7)
    else:
        if moveOfPlayer:
            for i in range(len(chessboard[1][0])):
                if colorama.Fore.BLUE + "WP" + colorama.Style.RESET_ALL in str(chessboard[1][0][i]):
                    newPieceInsteadOfPawn(True, i, 0, True, historyPawnIndex)
                    historyPawnIndex += 1
        else:
            for i in range(len(chessboard[0][7])):
                if colorama.Fore.RED + "BP" + colorama.Style.RESET_ALL in str(chessboard[0][7][i]):
                    newPieceInsteadOfPawn(False, i, 7, True, historyPawnIndex)
                    historyPawnIndex += 1

def newPieceInsteadOfPawn(whiteOrBlack, posX, posY, goingThroughHistory = False, historyPawnIndex = 0):
    '''
    Instances a new Piece intstead of the pawn at the posistion given'''
    global chessboard
    global history
    if not goingThroughHistory:
        chessboard[int(whiteOrBlack)][posY][posX] = " "
        newPiece = getValidInputForNewEndPiece()
        chessboard[int(whiteOrBlack)][posY][posX] = newPiece(posX, posY, whiteOrBlack)
        history[1].append(newPiece)
    else:
        chessboard[int(whiteOrBlack)][posY][posX] = " "
        newPiece = history[1][historyPawnIndex]
        chessboard[int(whiteOrBlack)][posY][posX] = newPiece(posX, posY, whiteOrBlack)

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

def undoMoves(countOfMovesToUndo):
    global chessboard
    global moveOfPlayer
    global history
    global historyPawnIndex
    historyPawnIndex = 0
    moveOfPlayer = True
    whiteBoard = createWhiteSide()
    blackBoard = createBlackSide()
    chessboard = [blackBoard, whiteBoard]
    for i in range(len(history[0])-countOfMovesToUndo):
        playersMove = history[0][i]
        chessboard = movePiece(playersMove[0], playersMove[1], chessboard)
        checkIfPawnAtEnd(True)
        moveOfPlayer = not moveOfPlayer
    history[0] = history[0][:-countOfMovesToUndo]
    printBoard(mergeBoards(chessboard))

def askForRemis():
    clear()
    if moveOfPlayer:
        print("Do you (White Player) want to ask the Black Player to agree on a draw?\nIf yes please write 'Yes, I want a draw'")
        inputOfPlayer = input()
        if inputOfPlayer == "Yes, I want a draw":
            print("\nDo you (Black Player) agree on the draw, the white Player asked for?\nIf you do so please write 'Yes, I agree on a draw'")
            inputOfPlayer = input()
            if inputOfPlayer == "Yes, I agree on a draw":
                print("\nYou both agreed on a draw")
                exit()
    else:
        print("Do you (Black Player) want to ask the Black Player to agree on a draw?\nIf yes please write 'Yes, I want a draw'")
        inputOfPlayer = input()
        if inputOfPlayer == "Yes, I want a draw":
            print("\nDo you (White Player) agree on the draw, the white Player asked for?\nIf you do so please write 'Yes, I agree on a draw'")
            inputOfPlayer = input()
            if inputOfPlayer == "Yes, I agree on a draw":
                print("\nYou both agreed on a draw")
                exit()
    print("\n\nAt least one of you didn't agree to the draw, the game will continue\n\n")

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

# Create the history array
# First element stores all the moves
# Second one stores the selected stuff from Pawn at the end
history = [[], []]
historyPawnIndex = 0

# Print first board
printBoard(mergeBoards(chessboard))

while True:
    '''
    Main loop which gets called every turn
    '''
    possibleMoves = allPossibleMoves(chessboard, moveOfPlayer, True)
    if isCheckMate(possibleMoves): gameOver()
    playersMove = getValidInput(possibleMoves)
    history[0].append(playersMove)
    chessboard = movePiece(playersMove[0], playersMove[1], chessboard)
    checkIfPawnAtEnd()
    printBoard(mergeBoards(chessboard))
    moveOfPlayer = not moveOfPlayer
