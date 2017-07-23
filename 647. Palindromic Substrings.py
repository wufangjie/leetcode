class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = n = len(s)
        dp = [True] * n
        for i in range(1, n):
            for j in range(i):
                if dp[j + 1] and s[i] == s[j]:
                    print(i, j)
                    dp[j] = True
                    count += 1
                else: # do not forget this
                    dp[j] = False
        return count


print(Solution().countSubstrings("abc"))
print(Solution().countSubstrings("fdsklf"))
