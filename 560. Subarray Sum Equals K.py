from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = cur = 0
        pre = defaultdict(int)
        for elem in nums:
            count += pre.get(k - cur - elem, 0) + (elem == k)
            pre[-cur] += 1
            cur += elem
        return count



print(Solution().subarraySum([1,1,1], 2))
