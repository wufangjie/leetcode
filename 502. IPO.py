# import bisect # maybe not faster than sort
import heapq
from collections import defaultdict


class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        dct = defaultdict(list)
        for c, p in zip(Capital, Profits):
            dct[c].append(p)

        H, have_not_pushed = [], []
        for c in dct:
            dct[c].sort()
            if c <= W:
                H.append((-dct[c].pop(), c))
            else:
                have_not_pushed.append(c)

        # dct = {}
        # for c, p in zip(Capital, Profits):
        #     if c not in dct:
        #         dct[c] = []
        #     bisect.insort(dct[c], p)

        # H = []
        # have_not_pushed = []
        # for c in dct:
        #     if c <= W:
        #         H.append((-dct[c].pop(), c))
        #     else:
        #         have_not_pushed.append(c)

        have_not_pushed.sort(reverse=True)
        heapq.heapify(H)
        final = W
        while k and H:
            p, c = heapq.heappop(H)
            final -= p
            if dct[c]:
                heapq.heappush(H, (-dct[c].pop(), c))
            while have_not_pushed:
                c = have_not_pushed[-1]
                if c <= final:
                    have_not_pushed.pop()
                    heapq.heappush(H, (-dct[c].pop(), c))
                else:
                    break
            k -= 1
        return final




# 看了半天才明白题目, 一开始以为要总的赚到的钱 (名声) 最多, 不包括用掉的
print(Solution().findMaximizedCapital(2, 3, [5,7,100], [0,3,9]))
