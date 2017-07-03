'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 1

        for i, elem in enumerate(nums):
            if nums[i] > i + 1:
                j = nums[i] - 1
                nums[i] = -1
                while j < n and j > -1 and nums[j] != j + 1:
                    k = nums[j] - 1
                    nums[j] = j + 1
                    j = k
            elif nums[i] > 0:
                nums[nums[i] - 1] = nums[i]

        for i, elem in enumerate(nums, 1):
            if i != elem:
                return i
        return i + 1


if __name__ == '__main__':
    assert Solution().firstMissingPositive([3, 4, -1, 1]) == 2
