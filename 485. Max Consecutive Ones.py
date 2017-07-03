class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        pre = -1 if nums[0] == 1 else 0
        theMax = 0
        for i in range(1, len(nums)):
            if nums[i] == 0:
                theMax = max(theMax, i - 1 - pre)
                pre = i
        return max(theMax, i - pre)


print(Solution().findMaxConsecutiveOnes([1,1,1,1,0,1,1,1,0]))
