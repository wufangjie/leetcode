class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        start = pre = theMax = 0

        for i in range(1, n):
            if nums[i] > nums[pre]:
                if i - start > theMax:
                    theMax = i - start
                pre = i
            else:
                start = pre = i
        return theMax + 1


print(Solution().findLengthOfLCIS([2,2,2,2,2]))
