from collections import deque, defaultdict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.used = 0
        self.dict = {}
        self.order = deque()
        self.counter = defaultdict(int)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            self.order.append(key)
            self.counter[key] += 1
        return self.dict.get(key, -1)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.dict:
            if self.used == self.capacity:
                while True:
                    k = self.order.popleft()
                    self.counter[k] -= 1
                    if self.counter[k] == 0:
                        self.dict.pop(k)
                        break
            else:
                self.used += 1

        self.dict[key] = value
        self.order.append(key)
        self.counter[key] += 1



if __name__ == '__main__':
    cache = LRUCache(2)
    print(cache.put(1, 1))
    print(cache.put(2, 2))
    print(cache.get(1))
    print(cache.put(3, 3))
    print(cache.get(2))
    print(cache.put(4, 4))
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
