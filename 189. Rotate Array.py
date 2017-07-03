class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]


# 破题, 说的不清不楚, 还要求余
nums = [1, 2]
Solution().rotate(nums, 3)
print(nums)
