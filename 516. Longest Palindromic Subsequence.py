from utils import memo


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # O(n) space 前面加一个本身就是的判断, 就能快很多, 也算技巧, 好吧
        n = len(s)
        dp = [[0] * n for _ in (1, 2)]
        for j in range(n):
            cur_row = j & 1
            pre_row = cur_row ^ 1
            dp[cur_row][j] = 1
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[cur_row][i] = 2 + dp[pre_row][i+1]
                else:
                    dp[cur_row][i] = max(dp[cur_row][i+1], dp[pre_row][i])
        return dp[cur_row][0]



        # # TLE 73/83, O(n^2) space
        # n = len(s)
        # dp = [[0] * n for _ in range(n)]
        # for j in range(n):
        #     dp[j][j] = 1
        #     for i in range(j - 1, -1, -1):
        #         if s[i] == s[j]:
        #             dp[i][j] = 2 + dp[i+1][j-1]
        #         else:
        #             dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        # return dp[0][-1]

        # # TLE 71/83
        # @memo
        # def rec(lo, hi):
        #     if hi == lo:
        #         return 1
        #     elif hi < lo:
        #         return 0
        #     if s[lo] == s[hi]:
        #         return 2 + rec(lo + 1, hi - 1)
        #     else:
        #         return max(rec(lo + 1, hi), rec(lo, hi - 1))
        # return rec(0, len(s) - 1)


import time
tic = time.time()
assert Solution().longestPalindromeSubseq("bbbab") == 4
assert Solution().longestPalindromeSubseq("cbbd") == 2
print(Solution().longestPalindromeSubseq("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"))
print(Solution().longestPalindromeSubseq("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"))
print(time.time() - tic)
