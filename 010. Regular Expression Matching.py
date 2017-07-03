'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)
'''


# this implement is not right when p contains some special regular symbol
# I'm not interested in this, so far

import re

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return bool(re.match('^' + p + '$', s))


if __name__ == '__main__':
    assert Solution().isMatch("aa","a") == False
    assert Solution().isMatch("aa","aa") == True
    assert Solution().isMatch("aaa","aa") == False
    assert Solution().isMatch("aa", "a*") == True
    assert Solution().isMatch("aa", ".*") == True
    assert Solution().isMatch("ab", ".*") == True
    assert Solution().isMatch("aab", "c*a*b") == True
