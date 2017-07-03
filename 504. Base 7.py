class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        num2 = abs(num)
        result = []
        while num2:
            result.append(str(num2 % 7))
            num2 //= 7
        if num < 0:
            result.append('-')
        result.reverse()
        return ''.join(result)
