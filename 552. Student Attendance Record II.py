class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 3
        elif n == 2:
            return 8
        elif n == 3:
            return 19

        to_mod = 1000000007
        dp = [1] * (n + 5)
        dp[1:3] = [2, 4]
        for i in range(3, n + 1):
            mid = i >> 1
            dp[i] = (dp[mid] * dp[i - mid - 1]
                     + dp[mid - 2] * dp[i - mid - 2]
                     + dp[mid - 1] * dp[i - mid - 3]
                     + dp[mid - 1] * dp[i - mid - 2]) % to_mod

        ret = dp[n] + dp[n - 1] * n
        # contain (P) LALL, LLAL, LLALL (P)

        half4 = (n - 5) >> 1
        for left in range(-1, half4):
            ret += 4 * dp[left] * dp[n - 6 - left]

        half5 = (n - 6) >> 1
        for left in range(-1, half5):
            ret += 2 * dp[left] * dp[n - 7 - left]

        if n & 1:
            ret += dp[half5] ** 2
        else:
            ret += 2 * dp[half4] ** 2

        return ret % to_mod


for i in range(5):
    print(Solution().checkRecord(i))


assert Solution().checkRecord(5) == 94
assert Solution().checkRecord(10) == 3536
