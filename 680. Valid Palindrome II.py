class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                # mid = (j - i + 1) >> 1
                # return (s[i:i+mid] == s[j-1:j-1-mid:-1]
                #         or s[i+1:i+1+mid] == s[j:j-mid:-1])
                return (s[i:j] == s[i:j][::-1]) or (s[j:i:-1] == s[i+1:j+1])
        return True


print(Solution().validPalindrome('abca'))
