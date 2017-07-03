import re


reg_fraction = re.compile('([+-]?\d+)/(\d+)')


class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        a0, b0 = 0, 1
        for pairs in reg_fraction.findall(expression):
            a, b = map(int, pairs)
            c = self.gcd(b0, b)
            a0 = a0 * (b // c) + a * (b0 // c)
            if a0 == 0:
                b0 = 1
            else:
                b0 *= b // c
                c = self.gcd(abs(a0), b0)
                a0 //= c
                b0 //= c
        return '{}/{}'.format(a0, b0)

    @staticmethod
    def gcd(a, b):
        if b > a:
            a, b = b, a
        while a % b != 0:
            a, b = b, a % b
        return b



assert Solution().fractionAddition("-1/2+1/2") == "0/1"
assert Solution().fractionAddition("-1/2+1/2+1/3") == "1/3"
assert Solution().fractionAddition("1/3-1/2") == "-1/6"
assert Solution().fractionAddition("5/3+1/3") == "2/1"
assert Solution().fractionAddition("-5/2+10/3+7/9") == "29/18"
