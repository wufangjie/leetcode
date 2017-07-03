import heapq


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min2 = heapq.nsmallest(2, nums)
        max3 = heapq.nlargest(3, nums)
        return max(max3[0] * max3[1] * max3[2],
                   max3[0] * min2[0] * min2[1])
        # if max3[0] < 0 or min2[0] * min2[1] <= max3[1] * max3[2]:
        #     return max3[0] * max3[1] * max3[2]
        # else:
        #     return max3[0] * min2[0] * min2[1]
