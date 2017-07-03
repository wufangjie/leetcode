'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

def _move_right(sorted_list, lo, hi, val):
    while lo < hi:
        lo += 1
        if sorted_list[lo] != val:
            break
    return lo


def _move_left(sorted_list, lo, hi, val):
    while lo < hi:
        hi -= 1
        if sorted_list[hi] != val:
            break
    return hi


def twoSum(sorted_list, lo, hi, theSum):
    while lo < hi:
        test = sorted_list[lo] + sorted_list[hi]
        if test == theSum:
            yield [sorted_list[lo], sorted_list[hi]]
            lo = _move_right(sorted_list, lo, hi, sorted_list[lo])
            hi = _move_left(sorted_list, lo, hi, sorted_list[hi])
        elif test > theSum:
            hi = _move_left(sorted_list, lo, hi, sorted_list[hi])
        else:
            lo = _move_right(sorted_list, lo, hi, sorted_list[lo])


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        theMax = len(nums) - 1
        pre = float('inf')
        results = []
        for i, a in enumerate(nums[:-2], 1):
            if a > 0:
                break
            if a != pre:
                pre = a
                for comb in twoSum(nums, i, theMax, -a):
                    results.append([a] + comb)
        return results


if __name__ == '__main__':
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
