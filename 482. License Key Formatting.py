class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '').upper()
        n = len(S)
        start = n % K
        result = [S[:start]] if start else []
        for i in range(start, n, K):
            result.append(S[i:i+K])
        return '-'.join(result)

print(Solution().licenseKeyFormatting("a-a-a-a-", 1))
print(Solution().licenseKeyFormatting("2-4A0r7-4k", 4))
