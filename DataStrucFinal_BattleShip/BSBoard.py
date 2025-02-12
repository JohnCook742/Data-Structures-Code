import random
import BSShip


# these classes are designed to handle
# the creation, storage, and display
# of the Battleship game grid
class GridPoint:
    def __init__(self):
        self.hit = False
        self.shipNode = BSShip.Node()
        self.char = '~'

    def hitUpdate(self):
        self.hit = True
        self.shipNode.hit = True
        if self.shipNode.parent is not None:
            self.char = '*'
            self.sunkUpdate()
        else:
            self.char = '_'

    def sunkUpdate(self):
        # print("Checking status of ship " + ship.displayID)
        if self.shipNode.parent is not None:
            ship = self.shipNode.parent
            if ship.checkStatus():
                self.char = ship.displayID


class GameBoard:
    def __init__(self, size=10):
        self.gridSize = size
        self.outerList = []
        for i in range(self.gridSize):
            self.outerList.append([])
            for j in range(self.gridSize):
                self.outerList[i].append(GridPoint())

    def checkPlacement(self, row: int, col: int, vert: bool, size: int):
        if row >= self.gridSize or col >= self.gridSize:
            return False
        elif size <= 0:
            return True
        elif self.outerList[row][col].shipNode.parent is None:
            if vert:
                row += 1
            else:
                col += 1
            return self.checkPlacement(row, col, vert, size - 1)

        return False

    def placeShip(self, ship: BSShip.Ship, newRow: int, newCol: int, newVert: bool) -> object:
        ship.row = newRow
        ship.col = newCol
        ship.vertOrientation = newVert
        shipNode = ship.head

        row = newRow
        col = newCol
        while shipNode is not None:

            self.outerList[row][col].shipNode = shipNode
            if newVert:
                row += 1
            else:
                col += 1
            shipNode = shipNode.next
        return self

    def displayBoard(self):
        print("\\|", end='')
        for i in range(self.gridSize):
            print(chr(i + ord('A')), end='')
            print("|", end='')
        print()
        for i in range(self.gridSize):
            print(i, end='')
            print("|", end='')
            for j in range(self.gridSize):
                self.outerList[i][j].sunkUpdate()
                print(self.outerList[i][j].char, end='')
                print("|", end='')
            print()
        print()

    def vertConverter(self, direction: str) -> bool:
        validVertical = ["v", "V"]
        validHorizon = ["h", "H"]
        for v in validVertical:
            if direction == v:
                return True
        for h in validHorizon:
            if direction == h:
                return False
        return self.vertConverter(input("Please input a valid direction (v/h): "))

    # converts [alpha][number] grid coordinate
    # into array indexes in tuple (row, col) format
    # ex: "c7", "3g", "37", or "CG" -> (3,7)
    def coordConverter(self, rawCoord: str) -> tuple:
        char_0 = ord('0')  # 48
        char_A = ord('A')  # 65
        char_a = ord('a')  # 97

        row = ord(rawCoord[0])
        col = ord(rawCoord[1])

        if row >= char_a:
            row -= char_a
        elif row >= char_A:
            row -= char_A
        elif row >= char_0:
            row -= char_0

        if col >= char_a:
            col -= char_a
        elif col >= char_A:
            col -= char_A
        elif col >= char_0:
            col -= char_0

        if row < self.gridSize and col < self.gridSize:
            return row, col
        return self.coordConverter(input("Please input valid grid coordinate (A#): "))

    # a move made by a human player against this board (ex: p1's move against p2's board)
    def playerMove(self) -> bool:
        # test to make sure player can make a move just in case
        canPlay = False
        for col in self.outerList:
            for node in col:
                if not node.hit:
                    canPlay = True
                    break
            if canPlay:
                break
        if not canPlay:
            return True

        invalidHit = True
        while invalidHit:
            shotCoord = (self.coordConverter
                         (input("Please enter the coordinate you would like to shoot (@#): ")))
            row = shotCoord[1]
            col = shotCoord[0]
            if not self.outerList[row][col].hit:
                self.outerList[row][col].hitUpdate()
                print("Shooting " + chr(65 + col) + str(row) + " ...")
                invalidHit = False

                if self.outerList[row][col].shipNode.parent is not None:
                    print("Hit")
                    self.displayBoard()
                    print("BONUS MOVE")
                    return self.playerMove()
            else:
                print("This coordinate may not be shot (again).")
        return False
        # return self

    # a random move made by the computer against this board (ex: p1's move against p2's board)
    # returns True if a ship was hit, False if no ship was hit
    def computerMove(self) -> bool:
        for i in range(self.gridSize * self.gridSize):
            row = random.randint(0, self.gridSize - 1)
            col = random.randint(0, self.gridSize - 1)
            if not self.outerList[row][col].hit:
                self.outerList[row][col].hitUpdate()
                print("Shooting " + chr(65 + col) + str(row) + " ...")

                if self.outerList[row][col].shipNode.parent is not None:
                    print("Hit")
                    self.displayBoard()
                    return self.smartMove(row, col, random.choice([True, False]))
                return False
        return True

    # a move made in a direction relative to a given coordinate
    # used to help find nearby ship nodes after getting a positive hit
    # returns true if valid adjacent node was a hit ship
    # returns false if not able to find a valid adjacent node to shoot or missed

    def smartMove(self, row: int, col: int, vert: bool) -> bool:
        print("BONUS MOVE")
        tempRow = row
        tempCol = col
        if vert:
            if row > 0 and not self.outerList[row-1][col].hit:
                row -= 1
            elif row < self.gridSize-1 and not self.outerList[row+1][col].hit:
                row += 1
        else:
            if col > 0 and not self.outerList[row][col-1].hit:
                col -= 1
            elif col < self.gridSize-1 and not self.outerList[row][col+1].hit:
                col += 1
        if not (tempRow == row or tempCol == col):
            self.outerList[row][col].hitUpdate()
            print("Shooting " + chr(65 + col) + str(row) + " ...")

            if self.outerList[row][col].shipNode.parent is not None:
                print("Hit")
                self.displayBoard()
                return self.smartMove(row, col, random.choice([True, False]))
            return False
        return self.computerMove()
