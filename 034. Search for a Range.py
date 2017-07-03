'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

def binary_search(nums, lo, hi, target):
    while lo <= hi:
        mid = (lo + hi) >> 1
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hi = len(nums) - 1
        pos = binary_search(nums, 0, hi, target)
        if pos > hi or nums[pos] != target:
            return [-1, -1]

        pos_l = binary_search(nums, 0, pos - 1, target - 0.5)
        pos_r = binary_search(nums, pos + 1, hi, target + 0.5)
        return [pos_l, pos_r - 1]


if __name__ == '__main__':
    nums = [0, 0, 0, 0, 1, 2, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8]
    assert Solution().searchRange(nums, 6) == [10, 12]
    assert Solution().searchRange([], 6) == [-1, -1]
