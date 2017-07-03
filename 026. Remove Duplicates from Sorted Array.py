'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = len(nums)
        cur = cur2 = 0
        while cur2 < maxlen:
            cur2 += 1
            while cur2 < maxlen and nums[cur2] == nums[cur2 - 1]:
                cur2 += 1
            nums[cur] = nums[cur2 - 1]
            cur += 1
        return cur


if __name__ == '__main__':

    nums = [1, 1, 2]
    hi = Solution().removeDuplicates(nums)
    assert nums[:hi] == [1, 2]
    nums = [1, 2, 3]
    hi = Solution().removeDuplicates(nums)
    assert nums[:hi] == [1, 2, 3]
    nums = [1, 1, 1, 2, 2, 2, 2, 3, 7, 7, 9]
    hi = Solution().removeDuplicates(nums)
    assert nums[:hi] == [1, 2, 3, 7, 9]
    nums = [1, 1, 1, 2, 2, 2, 2, 3, 7, 7, 9, 9]
    hi = Solution().removeDuplicates(nums)
    assert nums[:hi] == [1, 2, 3, 7, 9]
