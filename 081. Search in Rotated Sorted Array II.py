'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
'''

# def check(nums, lo, hi):
#     if lo == hi:
#         return 0
#     if nums[lo] == nums[hi]:
#         mid = (lo + hi) >> 1
#         if nums[mid] > nums[lo]:
#             return 1
#         elif nums[mid] < nums[hi]:
#             return -1
#         else:
#             check(nums, lo, mid)
#             pass
#     else:

#     mid = (lo + hi) >> 1

#     if lo == hi:
#         return True
#     if nums[lo] != nums[hi]:
#         return False
#     else:
#         mid = (lo + hi) >> 1
#         return check_all_the_same(nums, lo, mid) or check_all_the_same(nums, lo, mid) or




def binary_search(nums, lo, hi, target):
    while lo <= hi:
        mid = (lo + hi) >> 1
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return False


def search_rec(nums, lo, hi, target):
    if lo > hi:
        return False

    if nums[hi] > nums[lo]:
        return binary_search(nums, lo, hi, target)

    mid = (lo + hi) >> 1
    if nums[mid] == target:
        return True

    if nums[lo] == nums[hi] == nums[mid]:
        return (search_rec(nums, mid + 1, hi - 1, target) or
                search_rec(nums, lo + 1, mid - 1, target))
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
        :rtype: bool
        """
        return search_rec(nums, 0, len(nums) - 1, target)


if __name__ == '__main__':
    assert Solution().search([1, 1, 1, 1, 1, 3, 1, 1], 3) == True
    assert Solution().search([1, 1, 3, 1, 1, 1, 1, 1], 3) == True
    assert Solution().search([3, 4, 6, 1, 2, 2, 3, 3], 5) == False
