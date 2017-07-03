'''
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''

        maxlen = len(s)
        mini = ([(i - 1, i + 1) for i in range(1, maxlen - 1)
                 if s[i - 1] == s[i + 1]] +
                [(i - 1, i) for i in range(1, maxlen) if s[i - 1] == s[i]])

        def _expand(lo, hi):
            while lo >= 0 and hi < maxlen:
                if s[lo] != s[hi]:
                    return lo + 1, hi - 1
                lo -= 1
                hi += 1
            else:
                return lo + 1, hi - 1

        if mini:
            lo, hi = min((_expand(i, j) for i, j in mini), key=lambda x: x[0] - x[1])
            return s[lo:hi+1]
        else:
            return s[0]

        # lo = hi = theMax = 0
        # for i, j in (_expand(i, j) for i, j in mini):
        #     if j - i > theMax:
        #         lo, hi, theMax = i, j, j - i
        # return s[lo:hi+1]
        # # temp = sorted(
        # #               key=lambda x: x[0] - x[1])
        # # if temp:
        # #     return s[temp[0][0]:temp[0][1] + 1]
        # # else:
        # #     return s[0]


if __name__ == '__main__':
    assert Solution().longestPalindrome('') == ''
    assert Solution().longestPalindrome('w') == 'w'
    assert Solution().longestPalindrome('ww') == 'ww'
    assert Solution().longestPalindrome('www') == 'www'
    assert Solution().longestPalindrome('xwxy') == 'xwx'
