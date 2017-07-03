import random


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []
        self.count = 0

    def insert(self, val):
        """
        Inserts a value to the dict. Returns true if the dict did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.dict[val] = self.count
            self.list.append(val)
            self.count += 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the dict. Returns true if the dict contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            #if self.dict[val] != self.count - 1:
            if val != self.list[-1]:
                self.dict[self.list[-1]] = self.dict[val]
                self.list[self.dict[val]] = self.list[-1]
            self.dict.pop(val)
            self.list.pop()
            self.count -= 1
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the dict.
        :rtype: int
        """
        return self.list[random.randint(0, self.count - 1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
