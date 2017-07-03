from collections import defaultdict
from copy import deepcopy
from utils import memo


class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        @memo
        def rec(pos, left): # actually left can be just a number
            if not left:
                return 1
            l = left[-1]
            ret = 0
            for i, p in enumerate(pos):
                if p % l == 0 or l % p == 0:
                    ret += rec(tuple(pos[:i] + pos[i+1:]), left[:-1])
            return ret

        pos = tuple(range(1, N + 1))
        return rec(pos, pos)
        # position = defaultdict(set)
        # for i in range(1, N + 1):
        #     for j in range(1, N + 1):
        #         if i % j == 0 or j % i == 0:
        #             position[i].add(j)

        # left = deepcopy(position)

        # def rec(position, count):
        #     if not position:
        #         count[0] += 1
        #         return
        #     k = min(position.keys(), key=lambda x: len(position[x]))
        #     if len(position[k]) == 0:
        #         return
        #     position2 = position.copy()
        #     position2.pop(k)
        #     for u in position[k]:
        #         position3 = deepcopy(position2)
        #         for v in left[u]:
        #             if v in position3:
        #                 position3[v].remove(u)
        #         rec(position3, count)

        # count = [0]
        # rec(position, count)
        # return count[0]


import time
tic = time.time()
#print(Solution().countArrangement(6))
print(Solution().countArrangement(15))
print(time.time() - tic)
