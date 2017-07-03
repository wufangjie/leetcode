from collections import defaultdict


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.value = {}
        self.count = defaultdict(int)
        self.seq = []
        self.freq_span = defaultdict(int)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.capacity != 0 and key in self.count:
            self.move_forward(key)
            return self.value[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return

        if not self.seq:
            self.seq.append(key)
            self.freq_span[1] = [0, 0]
            self.count[key] += 1
        elif key not in self.count:
            cp = self.count[self.seq[-1]]
            if len(self.seq) != self.capacity:
                add = True
                self.seq.append(key)
            else:
                add = False
                self.count.pop(self.seq[-1])

            if cp == 1:
                self.seq[self.freq_span[1][0]+1 :] = self.seq[
                    self.freq_span[1][0] : -1]
                self.seq[self.freq_span[1][0]] = key
                self.freq_span[1][1] += add
            else:
                self.freq_span[1] = [self.freq_span[cp][1] + add] * 2
                if not add:
                    self.seq[-1] = key
                    if self.freq_span[cp][1] == self.freq_span[cp][0]:
                        self.freq_span.pop(cp)
                    else:
                        self.freq_span[cp][1] -= 1
            self.count[key] += 1
        else:
            self.move_forward(key)

        self.value[key] = value

    def move_forward(self, key):
        ck = self.count[key]
        self.count[key] += 1
        a, b = self.freq_span[ck]
        for i in range(b, a - 1, -1):
            if self.seq[i] == key:
                break

        if ck + 1 in self.freq_span:
            self.freq_span[ck + 1][1] += 1
        else:
            self.freq_span[ck + 1] = self.freq_span[ck][:1] * 2

        if self.freq_span[ck][1] == self.freq_span[ck][0]:
            self.freq_span.pop(ck)
        else:
            self.freq_span[ck][0] += 1

        self.seq[self.freq_span[ck + 1][0]+1 : i+1] = self.seq[
            self.freq_span[ck + 1][0] : i]
        self.seq[self.freq_span[ck + 1][0]] = key



    # def __init__(self, capacity):
    #     """
    #     :type capacity: int
    #     """
    #     self.capacity = capacity
    #     self.value = {}
    #     self.count = defaultdict(int)
    #     self.min = float('-inf')
    #     self.max = float('inf')
    #     self.count[self.max] = self.max
    #     self.bigger = {self.min: self.max}
    #     self.smaller = {self.max: self.min}

    # def get(self, key):
    #     """
    #     :type key: int
    #     :rtype: int
    #     """
    #     if self.capacity == 0:
    #         return -1

    #     if key in self.count:
    #         self.count[key] += 1
    #         self.move_forward(key)
    #         return self.value[key]
    #     else:
    #         return -1

    # def put(self, key, value):
    #     """
    #     :type key: int
    #     :type value: int
    #     :rtype: void
    #     """
    #     if self.capacity == 0:
    #         return

    #     self.value[key] = value

    #     if key not in self.count:
    #         if len(self.count) == self.capacity + 1:
    #             nxt = self.bigger[self.min]
    #         else:
    #             nxt = self.min

    #         self.bigger[key] = self.bigger[nxt]
    #         self.smaller[self.bigger[nxt]] = key
    #         self.bigger[self.min] = key
    #         self.smaller[key] = self.min

    #         if self.min < nxt < self.max:
    #             self.count.pop(nxt)
    #             # self.value.pop(nxt)
    #             # self.bigger.pop(nxt)
    #             # self.smaller.pop(nxt)

    #     self.count[key] += 1
    #     self.move_forward(key)

    # def move_forward(self, key):
    #     pre = key
    #     while self.count[key] >= self.count[self.bigger[pre]]:
    #         pre = self.bigger[pre]

    #     if pre != key:
    #         a1, a2 = self.smaller[key], self.bigger[key]
    #         b2 = self.bigger[pre]

    #         self.bigger[a1] = a2
    #         self.smaller[a2] = a1
    #         self.bigger[pre] = key
    #         self.smaller[key] = pre
    #         self.bigger[key] = b2
    #         self.smaller[b2] = key



# NOTE: 在 cache 里 get 或 put 算一次, 移出 cache 之后计数清零

obj = LFUCache(2)
for i, (f, p) in enumerate(zip(["put","put","put","put","put","get","get","get","get","put","put","get"], [[1,1],[2,2],[1,1],[2,2],[3,3],[3],[1],[1],[1],[1,1],[2,2],[1]])):
    if f == 'put':
        obj.put(*p)
    else:
        print(obj.get(p[0]))


obj = LFUCache(3)
for i, (f, p) in enumerate(zip(["put","put","put","put","get","get","get","get","put","get","get","get","get","get"], [[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]])):
    if f == 'put':
        obj.put(*p)
    else:
        print(obj.get(p[0]))







# import time

# tic = time.time()

# obj = LFUCache(2408)
# for i, (f, p) in enumerate(zip(a, b)):
#     if f == 'put':
#         obj.put(*p)
#     else:
#         obj.get(p[0])
#         # print(obj.count)
#         # print(obj.bigger)
#         # print(obj.smaller)
#         # print(p[0], obj.get(p[0]))
# print(time.time() - tic)
