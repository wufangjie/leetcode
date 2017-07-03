from collections import Counter


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        longest = 0
        for k, v in count.items():
            longest = max(longest, v + count.get(k + 1, -v))
        return longest


# NOTE: exactly 1 not <= 1
