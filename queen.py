class Queen:



    def __init__(self, xPos, yPos):
        self.char = "Q"
        self.pos = [xPos, yPos]

    def isAvailable(self, x, y, chessboard):
        if chessboard[y][x] == " ":
            return True
        else:
            return False


    def checkForAvailableMoves(self, chessboard):
        self.availableMoves = []
        moveOffsetOptions = [-1, 0, 1]

        for i in range(len(moveOffsetOptions)):
            currentOffset = moveOffsetOptions[i]
            while True:
                if self.isAvailable(currentOffset, self.pos[1], chessboard):
                    self.availableMoves.append([i, self.pos[1]])
                    steps = 1
                    currentOffset = moveOffsetOptions[i]*steps
                    steps += 1
                else:
                    break

        return self.availableMoves