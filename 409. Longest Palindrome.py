class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        odd = set()
        for c in s:
            if c in odd:
                length += 2
                odd.remove(c)
            else:
                odd.add(c)
        return length + bool(odd)
