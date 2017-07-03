'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
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
    return -1


def search_rec(nums, lo, hi, target):
    if lo > hi:
        return -1

    if nums[hi] > nums[lo]:
        return binary_search(nums, lo, hi, target)

    mid = (lo + hi) >> 1
    if nums[mid] == target:
        return mid

    if nums[lo] <= target:
        if nums[mid] > nums[lo] and nums[mid] < target:  # left > right
            return search_rec(nums, mid + 1, hi, target)
        else:
            return search_rec(nums, lo, mid - 1, target)
    else:
        if nums[mid] < nums[lo] and nums[mid] > target:  # right > left
            return search_rec(nums, lo, mid - 1, target)
        else:
            return search_rec(nums, mid + 1, hi, target)


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return search_rec(nums, 0, len(nums) - 1, target)


if __name__ == '__main__':
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 7) == 3
    assert Solution().search([1], 0) == -1
    assert Solution().search([], 0) == -1
    assert Solution().search([3, 1], 1) == 1
    assert Solution().search([3, 1], 3) == 0
    assert Solution().search([1, 3], 3) == 1
