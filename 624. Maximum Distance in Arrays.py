import heapq


class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min2 = heapq.nsmallest(2, ((arr[0], i) for i, arr in enumerate(arrays)))
        max2 = heapq.nlargest(2, ((arr[-1], i) for i, arr in enumerate(arrays)))
        if min2[0][1] != max2[0][1]:
            return max2[0][0] - min2[0][0]
        else:
            return max(max2[1][0] - min2[0][0], max2[0][0] - min2[1][0])
