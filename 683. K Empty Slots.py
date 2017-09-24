import bisect


class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        pre = []
        k += 1
        for j, p in enumerate(flowers, 1):
            n = len(pre)
            i = bisect.bisect(pre, p, 0, n)
            if i != 0 and p - pre[i - 1] == k:
                return j
            if i != n and pre[i] - p == k:
                return j
            pre.insert(i, p)
        return -1



# print(Solution().kEmptySlots([1,3,2], 1), 2)
# print(Solution().kEmptySlots([1,2,3], 1), -1)


print(Solution().kEmptySlots([6,5,8,9,7,1,10,2,3,4], 2))
