#from collections import deque

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1032ms, seperate c and use set (faster than tuple even only two element)
        if not s or s[0] == '0':
            return 0
        dp_1 = 9 if s[0] == '*' else 1
        dp_2 = 1
        i, n = 1, len(s)
        while i < n:
            p, c = s[i - 1], s[i]
            i += 1
            if c == '0': # must in two
                if p == '*':
                    new = dp_2 * 2
                elif p in {'1', '2'}:
                    new = dp_2
                else:
                    return 0
            elif c == '*':
                new = dp_1 * 9
                if p == '*':
                    new += dp_2 * 15
                elif p == '1':
                    new += dp_2 * 9
                elif p == '2':
                    new += dp_2 * 6
            else:
                new = dp_1
                if p in {'*', '1'}:
                    new += dp_2
                if p in {'*', '2'} and c < '7':
                    new += dp_2
            dp_2, dp_1 = dp_1, new % 1000000007

        return dp_1


        # # 1529ms, less assignment is useless
        # if not s or s[0] == '0':
        #     return 0

        # dp = [1, 9 if s[0] == '*' else 1]
        # n = len(s)
        # cur = i = 1
        # while i < n:
        #     pre = cur
        #     cur ^= 1
        #     if s[i] == '0': # must in two
        #         if s[i - 1] == '*':
        #             new = dp[cur] * 2
        #         elif s[i - 1] == '1' or s[i - 1] == '2':
        #             new = dp[cur]
        #         else:
        #             return 0
        #     else:
        #         new = dp[pre] * (9 if s[i] == '*' else 1)

        #         if s[i - 1] == '*' or s[i - 1] == '1':
        #             new += dp[cur] * (9 if s[i] == '*' else 1)
        #         if s[i - 1] == '*' or s[i - 1] == '2':
        #             if s[i] == '*':
        #                 new += dp[cur] * 6
        #             elif s[i] < '7':
        #                 new += dp[cur]

        #     dp[cur] = new % 1000000007
        #     i += 1

        # return dp[cur]


        # # 1412ms
        # if not s or s[0] == '0':
        #     return 0
        # dp_1 = 9 if s[0] == '*' else 1
        # dp_2 = 1

        # for i in range(1, len(s)):
        #     if s[i] == '0': # must in two
        #         if s[i - 1] == '*':
        #             new = dp_2 * 2
        #         elif s[i - 1] == '1' or s[i - 1] == '2':
        #             new = dp_2
        #         else:
        #             return 0
        #     else:
        #         new = dp_1 * (9 if s[i] == '*' else 1)

        #         if s[i - 1] == '*' or s[i - 1] == '1':
        #             new += dp_2 * (9 if s[i] == '*' else 1)
        #         if s[i - 1] == '*' or s[i - 1] == '2':
        #             if s[i] == '*':
        #                 new += dp_2 * 6
        #             elif s[i] < '7':
        #                 new += dp_2

        #     dp_2, dp_1 = dp_1, new % 1000000007

        # return dp_1







assert Solution().numDecodings("*") == 9
assert Solution().numDecodings("1*") == 18
assert Solution().numDecodings('12*1231223212*131') == 33600
assert Solution().numDecodings("*1*1*0") == 404
assert Solution().numDecodings("1*72*") == 285
