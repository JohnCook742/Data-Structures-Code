
from node import Node

class AVL:
    def __init__(self):
        self.head = None

    # checks if lengths of branches from curNode
    # are within acceptable range (+/- 1)
    # then uses rotation method to correct the tree
    def balanceTree(self, curNode):
        if curNode is not None:
            heightL = self.heightRec(curNode.left,0)
            heightR = self.heightRec(curNode.right, 0)
            nodeDiff = heightL - heightR
            # rotations
            if nodeDiff < -1:
                rightNode = curNode.right
                if self.heightRec(rightNode.left, 0) > self.heightRec(rightNode.right, 0):  # double rotation check
                    curNode.right = self.rightRot(curNode.right)
                curNode = self.leftRot(curNode)     # left rotation
            elif nodeDiff > 1:
                leftNode = curNode.left
                if self.heightRec(leftNode.right, 0) > self.heightRec(leftNode.left, 0):    # double rotation check
                    curNode.left = self.leftRot(curNode.left)
                curNode = self.rightRot(curNode)    # right rotation
        return curNode

    def leftRot(self, curNode):
        tempA = curNode
        tempB = curNode.right
        tempA.right = tempB.left
        tempB.left = tempA
        return tempB

    def rightRot(self, curNode):
        tempA = curNode
        tempB = curNode.left
        tempA.left = tempB.right
        tempB.right = tempA
        return tempB

    def add(self, value):
        self.head = self.addRec(self.head, value)
        return self

    def addRec(self, curNode, value):
        if curNode is None:
            newNode = Node(value)
            return newNode
        if value < curNode.value:
            curNode.left = self.addRec(curNode.left, value)
        else:
            curNode.right = self.addRec(curNode.right, value)
        curNode = self.balanceTree(curNode)
        return curNode

    def remove(self, value):
        self.head = self.removeRec(self.head, value)
        return self

    def removeRec(self, curNode, value):
        if curNode is not None:
            if curNode.value == value:
                if curNode.left is None:
                    curNode = curNode.right
                else:
                    if curNode.right is None:
                        curNode = curNode.left
                    else:
                        tempRight = curNode.right
                        curNode = curNode.left
                        curNode.right = self.recombineRight(curNode.right, tempRight)
            elif curNode.value > value:
                curNode.left = self.removeRec(curNode.left, value)
            else:
                curNode.right = self.removeRec(curNode.right, value)
            curNode = self.balanceTree(curNode)

        return curNode

    def recombineRight(self, curNode, rightNode):
        if curNode is not None:
            curNode.right = self.recombineRight(curNode.right, rightNode)
            return curNode
        return rightNode

    def contains(self, value):
        return self.containsRec(self.head, value)

    def containsRec(self, curNode, value):
        if curNode is None:
            return False
        if curNode.value == value:
            return True
        if curNode.value > value:
            return self.containsRec(curNode.left, value)
        else:
            return self.containsRec(curNode.right, value)

    def size(self):
        return self.sizeRec(self.head)

    def sizeRec(self, curNode):
        if curNode is not None:
            count = 1
            count += self.sizeRec(curNode.left)
            count += self.sizeRec(curNode.right)
            return count
        return 0

    def asList(self):
        pyList = self.asListRec(self.head)

        return pyList

    def asListRec(self, curNode):
        tempList = []
        if curNode is not None:
            tempList.append(curNode.value)
            tempList = tempList + self.asListRec(curNode.left)
            tempList = tempList + self.asListRec(curNode.right)
        return tempList

    def height(self):
        return self.heightRec(self.head, 0)

    def heightRec(self, curNode, curHeight):
        if curNode is not None:
            curHeight += 1
            leftHeight = self.heightRec(curNode.left, curHeight)
            rightHeight = self.heightRec(curNode.right, curHeight)

            if leftHeight >= rightHeight:
                return leftHeight
            else:
                return rightHeight
        return curHeight
