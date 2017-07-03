import heapq


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        H = [(-nums[i], i) for i in range(k - 1)]
        heapq.heapify(H)

        for i, elem in enumerate(nums[k-1:], k-1):
            heapq.heappush(H, (-elem, i))
            while H[0][1] <= i - k:
                heapq.heappop(H)
            result.append(-H[0][0])
        return result

Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)

Solution().maxSlidingWindow([6, 5, 7, 5, 7, 6, 4, 8, 2, 0, 8, 3, 8, 0, 5, 6, 3, 7, 9, 0], 5)
