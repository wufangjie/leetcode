class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        k = min((n * (n - 1) >> 1) - k, k)
        if k == 0:
            return 1
        if k < 0:
            return 0

        dp = [[0] * (k + 1), [0] * (k + 1)]
        dp[0][0] = dp[1][0] = 1
        pre = 1
        for i in range(2, n + 1):
            cur, pre = pre, pre ^ 1
            pre_max_non_zero = (i - 1) * (i - 2) >> 1
            cur_max_non_zero = (i) * (i - 1) >> 1
            half = cur_max_non_zero >> 1
            cum = 1
            for j in range(1, k + 1):
                if j - i + 1 > pre_max_non_zero:
                    break
                elif j > half:
                    dp[cur][j] = dp[cur][cur_max_non_zero - j]
                else:
                    cum += dp[pre][j]
                    if j - i >= 0:
                        cum -= dp[pre][j - i]
                    dp[cur][j] = cum % 1000000007

        return dp[cur][k]


        # TLE 35/80
                    # dp[cur][j] = sum(dp[pre][max(j-i+1, 0) : j+1]) % 1000000007


assert Solution().kInversePairs(300, 100) == 86577949
assert Solution().kInversePairs(1, 1) == 0
assert Solution().kInversePairs(1000, 1000) == 663677020
