from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        threshold = len(nums) // k
        result, left = [], []
        for key, val in Counter(nums).items():
            if val >= threshold:
                result.append(key)
                k -= 1
            else:
                left.append((val, key))
        return result + list(map(lambda x: x[1], heapq.nlargest(k, left)))


print(Solution().topKFrequent([1,1,1,2,2,3], 2))
