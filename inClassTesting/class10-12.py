class OpenAddressing:
    def __init__(self):
        self.list = [None] * 2
        self.length = 0

    def hash(self, value, size):
        return value % size

    def rehash(self, desired_size):
        new_list = [None] * desired_size
        for i in range(len(self.list)):
            value = self.list[i]
            if value is None:
                continue
            hash = self.hash(value, desired_size)
            j = i
            while new_list[j] is not None:
                j += 1
                j = j % desired_size
                if j == hash:
                    print("Error, you should not get here!")
                    break
            new_list[j] = value

    def add(self, value):
        if self.length >= len(self.list):
            self.rehash(len(self.list) * 2)
        hash = self.hash(value, len(self.list))
        j = hash
        while self.list[j] is not None:
            j += 1
            j = j % len(self.list)
            if j == hash:
                print("Error, you should not get here!")
                break
        self.list[j] = value
        self.length += 1

    def contains(self, value):
        hash = self.hash(value, len(self.list))
        j = hash
        while self.list[j] is not None and self.list[j] != value:
            j += 1
            if j >= len(self.list):
                j = 0
            if j == hash:
                return False
        if self.list[j] is None:
            return False
        return True


    def size(self):
        return self.length
    def remove(self, value):
        to_rehash = self.asList()
        to_rehash.remove(value)
        new_list = [None] * len(self.list)
        for i in range(len(to_rehash)):
            v =self.list[i]
            hash = self.hash(v, len(to_rehash))

        pass
    def asList(self):
        return self.list.copy()


open_addressing = OpenAddressing()
open_addressing.add(8)
open_addressing.add(88)
open_addressing.add(888)
open_addressing.add(8888)
print(open_addressing.asList())