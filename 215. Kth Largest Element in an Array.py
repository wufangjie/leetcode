import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if (n >> 1) >= k:
            return heapq.nlargest(k, nums)[-1]
        else:
            return heapq.nsmallest((n+1-k), nums)[-1]



import numpy as np

#a = np.random.randint(0, 99, 20)
Solution().findKthLargest(a, 13)
