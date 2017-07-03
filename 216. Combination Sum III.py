class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        theMin = max(1, n - (9 + 9 - k + 2) * (k - 1) // 2)
        theMax = min(9, n - (1 + k - 1) * (k - 1) // 2)

        def rec(k, n, m):
            if k == 1:
                if m <= n <= 9:
                    return [[n]]
                else:
                    return []
            results = []
            for i in range(m, theMax):
                for comb in rec(k-1, n-i, i+1):
                    results.append([i] + comb)
            return results
        return rec(k, n, theMin)

Solution().combinationSum3(3, 7)
