'''
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        maxlen = len(nums)
        cur = cur2 = 0
        while True:
            try:
                while nums[cur2] == val:
                    cur2 += 1
            except IndexError:
                break
            nums[cur] = nums[cur2]
            cur += 1
            cur2 += 1
        return cur


if __name__ == '__main__':
    nums = []
    hi = Solution().removeElement(nums, 0)
    assert nums[:hi] == []
    nums = [1, 1, 2]
    hi = Solution().removeElement(nums, 0)
    assert nums[:hi] == [1, 1, 2]
    nums = [1, 2, 3]
    hi = Solution().removeElement(nums, 1)
    assert nums[:hi] == [2, 3]
    nums = [1, 1, 1, 2, 2, 2, 2, 3, 7, 7, 9]
    hi = Solution().removeElement(nums, 2)
    assert nums[:hi] == [1, 1, 1, 3, 7, 7, 9]
    nums = [1, 1, 1, 2, 2, 2, 2, 3, 7, 7, 9, 9]
    hi = Solution().removeElement(nums, 9)
    assert nums[:hi] == [1, 1, 1, 2, 2, 2, 2, 3, 7, 7]
