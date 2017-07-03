from utils import memo


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        theSum = sum(nums)
        if theSum & 1:
            return False
        nums = sorted(nums, reverse=True)
        mid = theSum >> 1
        n = len(nums)
        theMin = nums[-1]

        @memo
        def dfs(i, acc):
            if acc == mid:
                return True
            elif acc + theMin > mid or i > n - 1:
                return False

            return dfs(i + 1, acc + nums[i]) or dfs(i + 1, acc)
        return dfs(1, nums[0])
