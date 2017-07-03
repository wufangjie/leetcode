class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        s = list(s)
        for i in range(0, n, 2 * k):
            if n - i >= k:
                s[i:i+k] = s[i:i+k][::-1]
            else:
                s[i:] = s[i:][::-1]
        return ''.join(s)


print(Solution().reverseStr("abcdefg", 2))
