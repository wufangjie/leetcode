from collections import defaultdict


pre = [chr(i) for i in range(97, 123)]


class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        # NOTE: only p[i:j] be called substring
        # dp = {}
        # for c in p:
        #     dp[c] = dp.get(pre[ord(c) - 98], 0) + 1
        # return sum(dp.values())

        if not p:
            return 0

        max_dct = defaultdict(int)
        max_dct[p[0]] = 1
        last = 1
        for i in range(1, len(p)):
            if pre[ord(p[i]) - 98] == p[i - 1]:
                max_dct[p[i]] = max(max_dct[p[i]], last + 1)
                last += 1
            else:
                max_dct[p[i]] = max(max_dct[p[i]], 1)
                last = 1
        return sum(max_dct.values())




print(Solution().findSubstringInWraproundString("cac"))
print(Solution().findSubstringInWraproundString("zabzab"))
print(Solution().findSubstringInWraproundString("yhxtdobyly"))
