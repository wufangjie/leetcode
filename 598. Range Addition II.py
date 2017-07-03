class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        for i, j in ops:
            if i < m:
                m = i
            if j < n:
                n = j
        return m * n
        # for i, j in ops:
        #     m = min(m, i)
        #     n = min(n, j)
        # return m * n



print(Solution().maxCount(3, 3, [[2,2],[3,3]]))
