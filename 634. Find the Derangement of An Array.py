class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        p1, p2 = 1, 2
        for i in range(4, n + 1):
            if i & 1:
                p2 = (i - 1) * (p1 + p2) % 1000000007
            else:
                p1 = (i - 1) * (p1 + p2) % 1000000007
        return p2 if n & 1 else p1


        # # NOTE: actually make large dp is costly, only pre two are useful
        # dp = [0, 0, 1, 2] + [0] * n
        # for i in range(4, n + 1):
        #     dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % 1000000007
        # return dp[n]

        # # TLE 45/69
        # dp = [0, 0, 1, 2] + [0] * n
        # for i in range(4, n + 1):
        #     p = 1
        #     for j in range(i - 2, 1, -1):
        #         p = (p % 1000000007) * (j + 1)
        #         dp[i] += dp[j] * p
        #     dp[i] = (dp[i] + (p << 1)) % 1000000007
        # return dp[n]



print(Solution().findDerangement(4))
assert Solution().findDerangement(100) == 944828409
print(Solution().findDerangement(1999))
