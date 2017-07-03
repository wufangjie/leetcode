class Solution(object):
    charmap = {chr(65 + i): i for i in range(26)}
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        theSum = 0
        unit = 1
        for c in reversed(s):
            theSum += (self.charmap[c] + 1) * unit
            unit *= 26
        return theSum



if __name__ == '__main__':
    assert Solution().titleToNumber('A') == 1
    assert Solution().titleToNumber('Z') == 26
    assert Solution().titleToNumber('AA') == 27
    assert Solution().titleToNumber('BA') == 53
    assert Solution().titleToNumber('ADMJR') == 536346
