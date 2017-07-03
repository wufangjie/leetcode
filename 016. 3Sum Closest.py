'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
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


def twoSumClosest(sorted_list, lo, hi, target):
    bestSum, minError = 0, float('inf')
    while lo < hi:
        test = sorted_list[lo] + sorted_list[hi]
        if test == target:
            return test, 0
        else:
            if abs(target - test) < minError:
                minError = abs(target - test)
                bestSum = test
            if test > target:
                hi = _move_left(sorted_list, lo, hi, sorted_list[hi])
            else:
                lo = _move_right(sorted_list, lo, hi, sorted_list[lo])
    return bestSum, minError


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        bestSum, theMax = 0, len(nums) - 1
        pre = minError = float('inf')
        for i, a in enumerate(nums[:-2], 1):
            if a != pre:
                pre = a
                tempSum, tempError = twoSumClosest(nums, i, theMax, target - a)
                if tempError == 0:
                    return tempSum + a
                elif tempError < minError:
                    bestSum, minError = tempSum + a, tempError
        return bestSum


if __name__ == '__main__':
    assert Solution().threeSumClosest([-1, 0, 1, 2, -1, -4], 9) ==3
