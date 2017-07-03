'''
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

from functools import wraps
from copy import deepcopy

def memo(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper._cache = cache
    return wrapper


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        @memo
        def sub_rec(k):
            if k == -1:
                return [[]]
            result = deepcopy(sub_rec(k - 1))
            for sub in result:
                sub.append(nums[k])
            return sub_rec(k - 1) + result

        return sub_rec(len(nums) - 1)


if __name__ == '__main__':
    Solution().subsets([1, 2, 3, 5, 9, 7])
