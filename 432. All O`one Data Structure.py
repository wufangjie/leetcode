class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.max = object()
        self.min = object()
        self.value = {self.max: float('inf'), self.min: float('-inf')}
        self.bigger = {self.min: self.max}
        self.smaller = {self.max: self.min}

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.value:
            self.value[key] += 1
            big = key
            while self.value[key] > self.value[self.bigger[big]]:
                big = self.bigger[big]
            if key != big:
                self.exchange(key, big)
        else:
            self.bigger[key] = self.bigger[self.min]
            self.smaller[self.bigger[self.min]] = key
            self.bigger[self.min] = key
            self.smaller[key] = self.min
            self.value[key] = 1

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.value:
            if self.value[key] == 1:
                self.value.pop(key)
                self.bigger[self.smaller[key]] = self.bigger[key]
                self.smaller[self.bigger[key]] = self.smaller[key]
            else:
                self.value[key] -= 1
                small = key
                while self.value[key] < self.value[self.smaller[small]]:
                    small = self.smaller[small]
                if key != small:
                    self.exchange(small, key)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        ret = self.smaller[self.max]
        return '' if ret == self.min else ret

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        ret = self.bigger[self.min]
        return '' if ret == self.max else ret

    def exchange(self, a, b):
        if self.bigger[a] != b:
            a1, a2 = self.smaller[a], self.bigger[a]
            b1, b2 = self.smaller[b], self.bigger[b]
            self.smaller[a2], self.bigger[a1] = b, b
            self.smaller[b2], self.bigger[b1] = a, a
            self.smaller[a], self.bigger[a] = b1, b2
            self.smaller[b], self.bigger[b] = a1, a2
        else:
            a1, b2 = self.smaller[a], self.bigger[b]
            self.bigger[a1] = b
            self.smaller[b2] = a
            self.smaller[a], self.bigger[a] = b, b2
            self.smaller[b], self.bigger[b] = a1, a



# Your AllOne object will be instantiated and called as such:
obj = AllOne()
for i, (f, p) in enumerate(zip(["inc","inc","inc","inc","getMaxKey","inc","inc","inc","dec","inc","inc","inc","getMaxKey"], [["hello"],["goodbye"],["hello"],["hello"],[],["leet"],["code"],["leet"],["hello"],["leet"],["code"],["code"],[]])):
    if f == 'inc':
        obj.inc(p[0])
        print(i, 'inc', p[0])
    elif f == 'dec':
        obj.dec(p[0])
        print(i, 'dec', p[0])
    elif f == 'getMaxKey':
        print(obj.getMaxKey())
    else:
        print(obj.getMinKey())
