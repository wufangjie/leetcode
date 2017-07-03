class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = sorted(nums)
        n = len(nums)

        for i in range(n):
            if nums[i] != snums[i]:
                break
        else:
            return 0

        for j in range(n - 1, i, -1):
            if nums[j] != snums[j]:
                break
        return j - i + 1
