class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if min(nums) != 0:
            return 0
        theMax = max(nums)
        miss = theMax * (theMax + 1) // 2 - sum(nums)
        return miss if miss else theMax + 1


Solution().missingNumber
