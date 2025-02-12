"""
Node class for the binary search tree.
Unlike other projects, feel free to add additional functions here.
For example, it may be helpful to have a height() method, etc.
Some students prefer to implement the recursive add, remove, and contains functions
in Node while other keep the recursive functions in BST
"""


class Node:
    def __init__(self, value):
        self.value = value  # The value at this node
        self.left = None    # A link (if any) to a node with a lesser value
        self.right = None   # A link (if any) to a node with a greater value


"""
The actual binary search tree class. It will have one member variable, root, 
which is the first node (if there are any)
"""


class BST:

    """
    BST constructor. There is no need to change this function.
    """

    def __init__(self):
        self.root = None

    """
    Add a value to the BST. Do not change the return statement.
    Examples:
    < Empty BST > 
    add(1) ->
    ⌐-1-¬
    x   x                         

    ⌐-1-¬
    x   x
    add(2) ->
    ⌐-1-¬
    x   2
    
    ⌐-1-¬
    x   2
    add(0) ->
    ⌐-1-¬
    0   2

    ⌐-1-¬
    0   2
    add(3) ->
       ⌐---1---¬
    ⌐-0-¬    ⌐-2-¬
    x   x    x   3
    """

    def add(self, value):
        self.root = self.addRec(self.root, value)
        return self

    def addRec(self, curNode, value):
        if curNode is None:
            newNode = Node(value)
            return newNode
        if value < curNode.value:
            curNode.left = self.addRec(curNode.left, value)
        else:
            curNode.right = self.addRec(curNode.right, value)
        return curNode

    """
    Remove a value from the BST.
    The value may not exist, but there will never be duplicate values. Stop if you remove a value.
    Do not change the return statement.

    Examples:

       ⌐---1---¬
    ⌐-0-¬    ⌐-2-¬
    x   x    x   3
    remove(3) ->
    ⌐-1-¬
    0   2

    ⌐-1-¬
    0   2
    remove(0)
    ⌐-1-¬
    x   2
    
    ⌐-1-¬
    x   2
    remove(2) ->
    ⌐-1-¬
    x   x
    
    ⌐-1-¬
    x   x 
    remove(1) -> 
    < Empty BST >
    """

    def remove(self, value):
        self.root = self.removeRec(self.root, value)
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
        return curNode
    
    def recombineRight(self, curNode, rightNode):
        if curNode is not None:
            curNode.right = self.recombineRight(curNode.right, rightNode)
            return curNode
        return rightNode

    """
    True if the BST contains the given value, false otherwise.
    You will need to change the return statement
    """
    def contains(self, value):
        return self.containsRec(self.root, value)

    def containsRec(self, curNode, value):
        if curNode is None:
            return False
        if curNode.value == value:
            return True
        if curNode.value > value:
            return self.containsRec(curNode.left, value)
        else:
            return self.containsRec(curNode.right, value)

    """
    Return the number of values in the BST.
    You will need to change the return statement.
    """
    def size(self):
        return self.sizeRec(self.root)

    def sizeRec(self, curNode):
        if curNode is not None:
            count = 1
            count += self.sizeRec(curNode.left)
            count += self.sizeRec(curNode.right)
            return count
        return 0

    """
    Return the BST as a list.
    You need to use a pre-order traversal.
    You will need to modify the return statement.

    Examples:

    < Empty BST >
    asList() ->
    []

     ⌐-1-¬
     x   x
    asList()->
    [1]

    ⌐-1-¬
    0   2
    asList()->
    [1, 0, 2]

     ⌐---1---¬
    ⌐-0-¬   ⌐-2-¬
    x   x   x   3
    asList()->
    [1, 0, 2, 3]
    """
    def asList(self):
        pyList = self.asListRec(self.root)
        return pyList

    def asListRec(self, curNode):
        tempList = []
        if curNode is not None:
            tempList.append(curNode.value)
            tempList = tempList + self.asListRec(curNode.left)
            tempList = tempList + self.asListRec(curNode.right)
        return tempList

    """
    Return the height of the tree.
    You will need to modify the return statement.

    Examples:

    < Empty BST >
    height() -> 0


     ⌐-1-¬
     x   x
    height() ->
    1

     ⌐-1-¬
     x   2
    height() ->
    2

     ⌐-1-¬
     0   2
    height() ->
    2

      ⌐---1---¬
    ⌐-0-¬   ⌐-2-¬
    x   x   x   3
    height() ->
    3
    """

    def height(self):
        return self.heightRec(self.root, 0)

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
