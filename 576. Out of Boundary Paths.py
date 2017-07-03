from collections import defaultdict


class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        if N == 0:
            return 0
        dp = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        dp[i][j][0] = 1
        bound = defaultdict(int)
        for k in range(m):
            bound[k, 0] += 1
            bound[k, n - 1] += 1
        for k in range(n):
            bound[0, k] += 1
            bound[m - 1, k] += 1

        pre = 1
        count = 0
        for k in range(N):
            cur = pre
            pre = pre ^ 1
            for i in range(m):
                for j in range(n):
                    dp[i][j][cur] = (dp[i-1][j][pre] + dp[i+1][j][pre]
                                     + dp[i][j-1][pre] + dp[i][j+1][pre])
                    if dp[i][j][cur] >= 1000000007:
                        dp[i][j][cur] %= 1000000007
            for (i, j), way in bound.items():
                count += way * dp[i][j][pre]
            count %= 1000000007
        return count


assert Solution().findPaths(m = 2, n = 2, N = 2, i = 0, j = 0) == 6
assert Solution().findPaths(m = 1, n = 3, N = 3, i = 0, j = 1) == 12
