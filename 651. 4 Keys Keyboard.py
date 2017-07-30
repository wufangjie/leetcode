class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 7:
            return N
        dp = [[(6, 3)], [(4, 1)], [(5, 1)]]
        for i in range(7, N + 1):
            p = i % 3
            temp = [(dp[p][-1][0] << 1, dp[p][-1][0])]
            for a, b in dp[p - 1]:
                if a + b > temp[-1][0]:
                    temp.append((a + b, b))
            dp[p] = temp
        return dp[N % 3][-1][0]


# NOTE: nothing at first
print(Solution().maxA(11))
assert Solution().maxA(49) == 1048576
