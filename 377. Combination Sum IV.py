from utils import memo
from collections import deque


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target + 1):
            for elem in nums:
                if i - elem >= 0:
                    dp[i] += dp[i - elem]
        return dp[target]


        # @memo
        # def rec(target):
        #     if target == 0:
        #         return 1
        #     elif target < 0:
        #         return 0
        #     return sum(rec(target - elem) for elem in nums)
        # return rec(target)


        # n = len(nums)
        # def rec(target, i):
        #     if target == 0:
        #         return 1
        #     if i >= n:
        #         return 0
        #     return sum(rec(target - k * nums[i], i + 1)
        #                for k in range(target // nums[i] + 1))
        # return rec(target, 0)


assert Solution().combinationSum4([3,33,333], 10000) == 0
assert Solution().combinationSum4([4,2,1], 32) == 39882198
assert Solution().combinationSum4([1,2,3], 4) == 7

# negative and positive can not exist together and no zero

# combination?
# (1, 1, 1, 1)
# (1, 1, 2) ####
# (1, 2, 1) ####
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
