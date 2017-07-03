'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
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
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return binary_search(nums, 0, len(nums) - 1, target)


if __name__ == '__main__':
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
    assert Solution().searchInsert([1, 3, 5, 6], 0) == 0
    assert Solution().searchInsert([], 0) == 0
