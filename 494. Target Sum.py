from utils import memo


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)

        @memo
        def dfs(i, current):
            if i == n:
                return current == S
            return dfs(i + 1, current + nums[i]) + dfs(i + 1, current - nums[i])

        return dfs(0, 0)



assert Solution().findTargetSumWays([0], 0) == 2
assert Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
