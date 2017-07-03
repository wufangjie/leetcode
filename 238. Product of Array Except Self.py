class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1] * n
        for i in range(1, n): # before
            output[i] = output[i-1] * nums[i-1]
        after = 1
        for i in range(n-1, -1, -1):
            output[i] *= after
            after *= nums[i]
        return output


Solution().productExceptSelf([1,2,3,4])
