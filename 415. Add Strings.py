from itertools import izip_longest # for python2, zip_longest for python3


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        forward = 0
        for c1, c2 in zip_longest(reversed(num1), reversed(num2), fillvalue=0):
            temp = int(c1) + int(c2) + forward
            if temp > 9:
                forward = 1
                temp %= 10
            else:
                forward = 0
            result.append(str(temp))
        if forward:
            result.append('1')
        return ''.join(reversed(result))
