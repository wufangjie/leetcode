class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        pre = theMax = sum(nums[:k])
        for i in range(k, len(nums)):
            pre += nums[i] - nums[i - k]
            if pre > theMax:
                theMax = pre
        return theMax / (k + 0.0)
