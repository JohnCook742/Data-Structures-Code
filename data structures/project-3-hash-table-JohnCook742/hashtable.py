"""
For this assignment you need to implement a hash table using the following
class definitions. You may add additional functions as needed.
"""

"""
Hash Table Class:
The class that you will use to implement the hash table.
"""


class HashTable:
    """
    __init__
    Write a constructor that creates an empty hash table that is a list of lists.
    It should start with a length of 2. When you add your third item, it should grow to be of length 4,
    when you add your fifth item it should grow to length 8, etc.
    """

    def __init__(self):
        self.length = 0
        self.outerList = []
        for i in range(2):
            self.outerList.append([])

    # hash function that returns an index value
    # given a value that will go in the hash table
    def hash(self, value):
        # basic version
        hashIndex = value % len(self.outerList)
        return hashIndex

    """
    add function: Add an item to the hash table.
    Keep the 'return self' line at the end to help with testing.
    Also, to pass off, you need to grow your hash table whenever the current 
    number of entries equals the size of your internal list.
    For example, if you have a hash table whose size in RAM 2, if you add a third entry, you need to rehash.
    Everytime you grow your table, it should double in size.
    Also, you will hash values by taking the modulus of the incoming value and
    the length of the table, i.e. value % len(self.table)
    """

    def add(self, value):
        # check for rehash
        if self.length >= len(self.outerList):
            # print("rehashing") # debug
            newList = []
            oldList = self.outerList
            for i in range(2 * len(self.outerList)):
                newList.append([])
            self.outerList = newList
            for i in range(len(oldList)):
                for j in range(len(oldList[i])):
                    oldVal = oldList[i][j]
                    self.outerList[self.hash(oldVal)].append(oldVal)
        # get hash of incoming value
        # add value to inner list
        self.outerList[self.hash(value)].append(value)
        self.length = self.size()
        return self

    """
    size function: Return the number of items in the hash table.
    """

    def size(self):
        count = 0
        for i in range(len(self.outerList)):
            count += len(self.outerList[i])
        # print(count) debug
        return count


    """
    Return True if the list has a node with the same value as the provided
    value. Return False otherwise.
    """

    def contains(self, value):
        # get hash of incoming value
        outdex = self.hash(value)
        # check if list at that index contains the value
        for i in range(len(self.outerList[outdex])):
            if self.outerList[outdex][i] == value:
                return True
        return False

    """
    Remove an item from the hash table that has the same value as the provided value.
    You will never be asked to add duplicate items, so if you find a match, you can remove it and stop looking.
    If there is not an entry that matches value, do nothing.
    Keep the 'return self' line at the end to help with testing.
    """

    def remove(self, value):
        # get hash of incoming value
        outdex = self.hash(value)
        # remove at that index
        for i in range(len(self.outerList[outdex])):
            if self.outerList[outdex][i] == value:
                self.outerList[outdex].remove(value)
                break
        self.length = self.size()
        return self

    """
    Return the hash table as a python list.
    For example, if the code were:
    HashTable().add(1).asList()
    then the return value should be [1].
    In order to match the test cases, items should be added from the beginning of your
    internal list to the end.
    """

    def asList(self):
        pyList = []
        # loop over outer list
        for i in range(len(self.outerList)):
            # loop over inner list
            for j in range(len(self.outerList[i])):
                # add values to new list
                pyList.append(self.outerList[i][j])
        # print(pyList) # debug
        return pyList
