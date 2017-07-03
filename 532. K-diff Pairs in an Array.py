from collections import Counter


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return sum(1 for v in Counter(nums).values() if v > 1)
        elif k < 0:
            return 0

        unq = set(nums)
        return sum(1 for elem in unq if elem + k in unq)
