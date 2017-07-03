class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(elem) for elem in nums]
        if len(nums) <= 2:
            return '/'.join(nums)
        else:
            return nums[0] + '/(' + '/'.join(nums[1:]) + ')'
