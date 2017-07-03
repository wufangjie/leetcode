'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

def sub_rec(nums, selected=[], results=[]):
    if not nums:
        results.append(selected)
    else:
        sub_rec([], selected, results)
        pre = None
        for i, elem in enumerate(nums, 1):
            if elem != pre:
                sub_rec(nums[i:], selected + [elem], results)
                pre = elem


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        sub_rec(nums, [], results)
        return results


if __name__ == '__main__':
    Solution().subsetsWithDup([1, 2, 2, 3, 3])
