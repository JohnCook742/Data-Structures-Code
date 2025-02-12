class Node:
    def __init__(self, parent=None):
        self.parent = parent
        self.next = None
        self.hit = False


class Ship:
    def __init__(self, size: int, classID: str,
                 row: int = 0, col: int = 0,
                 vert: bool = False):
        self.sunk = False
        self.displayID = classID
        self.size = size
        self.head = Node(self)
        self.row = row
        self.col = col
        self.vertOrientation = vert
        # orientation of the ship:
        # True -> vertically oriented
        # False -> horizontally oriented

        curNode = self.head
        for i in range(size-1):
            curNode.next = Node(self)
            curNode = curNode.next

    # returns true if ship is sunk, false otherwise
    def checkStatus(self) -> bool:
        return self.checkRec(self.head)

    def checkRec(self, shipNode: Node) -> bool:
        if shipNode is not None:
            if shipNode.hit:
                return self.checkRec(shipNode.next)
            else:
                return False
        return True

