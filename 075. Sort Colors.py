'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
'''

from collections import Counter

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        j = 0
        for i in range(3):
            while count[i]:
                nums[j] = i
                count[i] -= 1
                j += 1

if __name__ == '__main__':
    nums = [0, 1, 2, 2, 1, 1, 0, 0, 0, 0]
    Solution().sortColors(nums)
    print(nums)
