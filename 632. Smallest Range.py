#import heapq
#from collections import deque
import bisect


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # first I use deque, but python2's deque do not support insert method
        n = len(nums)
        lens = [len(lst) for lst in nums]
        S = sorted([(-lst[0], i, 0) for i, lst in enumerate(nums)])
        theMin = float('inf'), 0
        while S:
            theMin = min(theMin, (S[-1][0] - S[0][0], -S[-1][0]))
            _, i, j = S.pop()
            if j == lens[i] - 1:
                break
            bisect.insort(S, (-nums[i][j + 1], i, j + 1))
        return [theMin[1], sum(theMin)]


print(Solution().smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]))

print(Solution().smallestRange([[4]]))
