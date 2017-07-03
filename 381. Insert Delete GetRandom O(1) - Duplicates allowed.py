import random
from collections import defaultdict


class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(set)
        self.list = []
        self.count = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        ret = False if self.dict[val] else True
        self.dict[val].add(self.count)
        self.list.append(val)
        self.count += 1
        return ret

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.dict[val]:
            i = self.dict[val].pop()
            if i != self.count - 1:
                self.list[i] = self.list[-1]
                self.dict[self.list[-1]].add(i)
                self.dict[self.list[-1]].remove(self.count -1)

            # the first bisect with defaultdict(list) method seems faster
            # than defaultdict(set) version
            # if val != self.list[-1]:
            #     bisect.insort(self.dict[self.list[-1]],
            #     self.list[self.dict[val][-1]] = self.list[-1]
            #     self.dict[self.list[-1]].pop()
            # self.dict[val].remove
            self.list.pop()
            self.count -= 1
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.list[random.randint(0, self.count - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()

# ["RandomizedCollection","insert","remove","insert"]
# [[],[1],[1],[1]]

for op, p in zip(["insert","insert","insert","insert","insert","remove","remove","remove","insert","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"], [[1],[1],[2],[2],[2],[1],[1],[2],[1],[2],[],[],[],[],[],[],[],[],[],[]]):
    if op == 'insert':
        print(obj.insert(p[0]))
    elif op == 'remove':
        print(obj.remove(p[0]))
    else:
        print(obj.getRandom())

#["insert","remove","insert"], [[1],[1],[1]]):
