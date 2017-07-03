class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count_zero = 0
        for i, elem in enumerate(nums):
            if elem == 0:
                count_zero += 1
            elif count_zero:
                nums[i - count_zero] = elem
        if count_zero:
            nums[-count_zero:] = [0] * count_zero

nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)
