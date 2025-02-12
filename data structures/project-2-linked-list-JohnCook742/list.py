"""
For this assignment you need to implement a linked list using the following
class definition. You may add addition functions as needed.
"""
import list

""""
Node Class:
Every item in your linked list will be encapsulated in this class.
value is the item encapsulated by the node. 
next is a pointer to the next node in line. This will be None if it is the last item in the list.
You do not need to edit the Node class to complete this assignment
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
Linked List Class:
The class that you will use to store your items.
Note, you may not use python's built in classes to implement these functions.
"""


class LinkedList:
    """
    LinkedList initialization:
    Creates a place for a head node (based on stack overflow posts)
    """

    def __init__(self):
        self.head = None

    """
    add function: Add an item to the linked list. You will need to wrap
    this value in a Node class. 
    Keep the 'return self' line at the end to help with testing.
    """

    def add(self, value):
        self.head = self.recAdd(value, self.head)
        return self  # Do not change this final line

    # based on class example post
    def recAdd(self, value, currentNode):
        if currentNode is None:
            return Node(value)
        else:
            currentNode.next = self.recAdd(value, currentNode.next)
            return currentNode

    """
    Remove an item from the list that has the same value as the provided value.
    You will never be asked to add duplicate items, so if you find a match, you can remove it and stop looking.
    If there is not a node with the given value, do nothing.
    Keep the 'return self' line at the end to help with testing.
    """

    def remove(self, value):
        self.head = self.recRemove(value, self.head)
        return self  # Do not change this final line

    # based on class example for add function and adapted
    def recRemove(self, value, currentNode):
        if currentNode is None:
            return None
        else:
            if currentNode.value == value:
                return currentNode.next
            else:
                currentNode.next = self.recRemove(value, currentNode.next)
                return currentNode

    """
    Return the number of nodes in the list. Return 0 if the list is empty.
    """

    def size(self):
        if self.head is None:
            return 0
        count = 1 + self.recSize(self.head.next)
        # debug stuff
        # print(count)
        # print(self.asList())
        return count

    def recSize(self, currentNode):
        if currentNode is None:
            return 0
        return 1 + self.recSize(currentNode.next)

    """
    Return True if the list has a node with the same value as the provided 
    value. Return False otherwise.
    """

    def contains(self, value):
        return self.recContains(value, self.head)

    def recContains(self, value, currentNode):
        if currentNode is None:
            return False
        else:
            if currentNode.value == value:
                return True
            else:
                return self.recContains(value, currentNode.next)

    """
    Return the linked list as a python list.
    For example, if the code were:
    LinkedList().add(1).asList()
    then the return value should be [1].
    """

    def asList(self):
        pyList = []
        if self.head is not None:
            pyList = pyList + self.recList(self.head)
        return pyList

    def recList(self, currentNode):
        tempList = [currentNode.value]
        if currentNode.next is not None:
            tempList = tempList + self.recList(currentNode.next)
        return tempList
