class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(range(len(nums)), key=lambda x: nums[x])
