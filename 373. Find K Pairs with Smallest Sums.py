import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n1, n2 = len(nums1), len(nums2)
        if n1 * n2 == 0:
            return []

        H = [(nums1[0] + nums2[0], 0, 0)]
        result = []
        pushed = set()
        while k > 0 and H:
            k -= 1
            _, i, j = heapq.heappop(H)
            result.append([nums1[i], nums2[j]])
            if i + 1 < n1 and (i + 1, j) not in pushed:
                heapq.heappush(H, (nums1[i + 1] + nums2[j], i + 1, j))
                pushed.add((i + 1, j))
            if j + 1 < n2 and (i, j + 1) not in pushed:
                heapq.heappush(H, (nums1[i] + nums2[j + 1], i, j + 1))
                pushed.add((i, j + 1))
        return result


print(Solution().kSmallestPairs([1,1,2], [1,2,3], 10))
