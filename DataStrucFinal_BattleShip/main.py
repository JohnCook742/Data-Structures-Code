import random
import BSShip
import BSBoard


class Fleet:
    def __init__(self, gameBoard: BSBoard.GameBoard):
        self.gameBoard = gameBoard
        air = BSShip.Ship(5, "A")
        btl = BSShip.Ship(4, "B")
        cru = BSShip.Ship(3, "C")
        sub = BSShip.Ship(3, "S")
        dst = BSShip.Ship(2, "D")
        self.fleetList = [air, btl, cru, sub, dst]

    # checks if entire fleet is sunk to signal game end
    # return False if fleet is not sunk
    # return True if fleet is sunk
    def checkFleet(self):
        for ship in self.fleetList:
            if not ship.checkStatus():
                return False
        return True

    def playerSetup(self) -> object:
        for ship in self.fleetList:
            shipCoord = (self.gameBoard.coordConverter
                         (input("Enter head location for ship " + ship.displayID +
                                " of size " + str(ship.size) + " (A#): ")))
            shipVert = (self.gameBoard.vertConverter
                        (input("Enter the orientation of the ship (v/h): ")))
            while not self.gameBoard.checkPlacement(shipCoord[1], shipCoord[0], shipVert, ship.size):
                print("This ship cannot be placed here.")
                shipCoord = (self.gameBoard.coordConverter
                             (input("Enter open head location for ship " + ship.displayID +
                                    " of size " + str(ship.size) + " (A#): ")))
                shipVert = (self.gameBoard.vertConverter
                            (input("Enter open orientation of the ship (v/h): ")))
            self.gameBoard.placeShip(ship, shipCoord[1], shipCoord[0], shipVert)
        print("Fleet has been placed.")

        return self.gameBoard

    def computerSetup(self) -> object:
        for ship in self.fleetList:
            shipVert = random.choice([True, False])
            shipCoord = self.generateCoord(ship.size, shipVert)
            self.gameBoard.placeShip(ship, shipCoord[0], shipCoord[1], shipVert)
        return self.gameBoard

    def generateCoord(self, size: int, vert: bool) -> tuple:
        boardSize = self.gameBoard.gridSize
        row = boardSize
        col = boardSize
        while not self.gameBoard.checkPlacement(row, col, vert, size):
            row = random.randint(0, boardSize-1)
            col = random.randint(0, boardSize-1)
        print("trying " + str(col) + ", " + str(row))
        return row, col


class GameMaster:
    def __init__(self, boardSize=10):
        self.size = boardSize
        # player 1 minimum setup
        self.p1Board = BSBoard.GameBoard(boardSize)
        self.p1Fleet = Fleet(self.p1Board)
        # self.p1Streak = False

        # player 2 minimum setup
        self.p2Board = BSBoard.GameBoard(boardSize)
        self.p2Fleet = Fleet(self.p2Board)
        # self.p2Streak = False

    # player vs player game
    def pvpGame(self):
        print("Starting human vs. human game ... ")
        print("Player 1 setup:")
        self.p1Board.displayBoard()
        self.p1Fleet.playerSetup()
        print("Player 2 setup:")
        self.p1Board.displayBoard()
        self.p2Fleet.playerSetup()
        print("Ships placed ... ")
        for i in range(self.size * self.size):
            if self.p1Fleet.checkFleet() or self.p2Fleet.checkFleet():
                continue
            # player 1 turn
            print("Player 1 turn " + str(i + 1) + ":")
            self.p2Board.displayBoard()
            if self.p2Board.playerMove():
                print("No moves left.")
                break
            else:
                print("Miss")
            self.p2Board.displayBoard()

            # player 2 turn
            print("Player 2 turn " + str(i + 1) + ":")
            self.p1Board.displayBoard()
            if self.p1Board.playerMove():
                print("No moves left.")
                break
            else:
                print("Miss")
            self.p1Board.displayBoard()

        self.gameEnd()

    # player vs computer game
    def pvcGame(self):
        print("Starting human vs. cpu game ... ")
        print("Player 1 setup:")
        self.p1Board.displayBoard()
        self.p1Fleet.playerSetup()
        self.p2Fleet.computerSetup()
        print("Ships placed ... ")
        for i in range(self.size * self.size):
            if self.p1Fleet.checkFleet() or self.p2Fleet.checkFleet():
                continue
            print("Human turn " + str(i + 1) + ":")
            self.p2Board.displayBoard()
            if self.p2Board.playerMove():
                print("No moves left.")
                break
            else:
                print("Miss")
            self.p2Board.displayBoard()
            print("CPU turn " + str(i + 1) + ":")
            if self.p1Board.computerMove():
                print("No moves left.")
                break
            else:
                print("Miss")
            self.p1Board.displayBoard()

        self.gameEnd()

    # computer vs computer game
    def cvcGame(self):
        print("Starting cpu vs. cpu game ... ")
        self.p1Fleet.computerSetup()
        self.p2Fleet.computerSetup()
        print("Ships placed ... ")
        for i in range(self.size * self.size):
            if self.p1Fleet.checkFleet() or self.p2Fleet.checkFleet():
                continue
            print("CPU1 turn " + str(i+1) + ":")
            if self.p2Board.computerMove():
                print("No moves left.")
                break
            else:
                print("Miss")
            self.p2Board.displayBoard()
            print("CPU2 turn " + str(i+1) + ":")
            if self.p1Board.computerMove():
                print("No moves left.")
                break
            else:
                print("Miss")
            self.p1Board.displayBoard()

        self.gameEnd()

    def gameEnd(self):
        if self.p1Fleet.checkFleet() and self.p2Fleet.checkFleet():
            print("Game ended in a draw.")
        elif self.p1Fleet.checkFleet():
            print("Player 2 wins.")
        elif self.p2Fleet.checkFleet():
            print("Player 1 wins.")
        else:
            print("Error")


gm = GameMaster()
print("Welcome to BATTLESHIP!")
print("")
print("Available game modes:")
print("0 - player vs player")
print("1 - player vs computer")
print("2 - computer vs computer")
inputNeeded = True
gameMode = 0
while inputNeeded:
    choice = str(input("Please select a game mode: "))
    if 48 <= ord(choice) < 48+3:
        gameMode = int(choice)
        inputNeeded = False
if gameMode == 0:
    gm.pvpGame()
elif gameMode == 1:
    gm.pvcGame()
elif gameMode == 2:
    gm.cvcGame()

else:
    print("Error")
print("Goodbye")
