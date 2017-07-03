from collections import Counter
import re


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        theMin = min(Counter(s).values())
        for i in range(2, 1 + theMin):
            if theMin % i == 0 and n % i == 0:
                # if re.match('({}){{{}}}'.format(s[:(n//i)], i), s):
                l = n // i
                first = s[:l]
                for j in range(l, n-1, l):
                    if s[j:j+l] != first:
                        break
                else:
                    return True
        return False


assert Solution().repeatedSubstringPattern("abab")
assert not Solution().repeatedSubstringPattern("aba")
assert Solution().repeatedSubstringPattern("abcabcabcabc")
assert Solution().repeatedSubstringPattern("bb")
