'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
            # for lo in xrange(lo + 1, hi + 1):
            #     if sorted_list[lo] != sorted_list[lo - 1]:
            #         break
            # for hi in xrange(hi - 1, lo - 1, -1):
            #     if sorted_list[hi] != sorted_list[hi + 1]:
            #         break



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


def nSum(sorted_list, lo, hi, target, n):
    if (hi - lo < n - 1 or target < sum(sorted_list[lo:lo + n]) or
        target > sum(sorted_list[hi - n + 1:hi + 1])):  # this pruning is important
        return
    if n == 2:
        for a, b in twoSum(sorted_list, lo, hi, target):
            yield [a, b]
    else:
        for i, elem in enumerate(sorted_list[lo:], lo):
            if i == lo or elem != sorted_list[i - 1]:
                for comb in nSum(sorted_list, i + 1, hi, target - elem, n - 1):
                    yield [elem] + comb


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return [list(comb) for comb in
                nSum(sorted(nums), 0, len(nums) - 1, target, 4)]


if __name__ == '__main__':
    print(Solution().fourSum([1,0,-1,0,-2,2], 0))
    print(Solution().fourSum([-1, 0, 1, 2, -1, -4], 0))
    print(Solution().fourSum([1, -5,  2, -8, -6, -5,  6,  8, -5, -7,  0,  6,  1,  4,  0,  7, -3, -3,  6, -9], 0))
