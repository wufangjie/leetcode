class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        seen = [False] * (n + 1)
        for i in nums:
            if seen[i]:
                break
            seen[i] = True
        return [i, (1 + n) * n // 2 + i - sum(nums)]
