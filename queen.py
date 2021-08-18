class Queen:



    def __init__(self, xPos, yPos):
        self.char = "Q"
        self.pos = [xPos, yPos]

    def isAvailable(self, x, y, chessboard):
        if x != -1 and y != -1 and y != len(chessboard) and x != len(chessboard[0]):
            if chessboard[y][x] == " ":
                return True
            else:
                return False
        else:
            return False


    def checkForAvailableMoves(self, chessboard):
        self.availableMoves = []
        moveOffsetOptions = [-1, 0, 1]

        for i in range(len(moveOffsetOptions)):
            currentOffset = moveOffsetOptions[i]
            steps = 1
            while True:
                if self.isAvailable(self.pos[0] + currentOffset, self.pos[1], chessboard):
                    self.availableMoves.append([self.pos[0] + currentOffset, self.pos[1]])
                    steps += 1
                    currentOffset = moveOffsetOptions[i]*steps
                else:
                    break
                    

        return self.availableMoves