class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        t = nums[len(nums) >> 1]
        return sum((abs(i - t) for i in nums))
