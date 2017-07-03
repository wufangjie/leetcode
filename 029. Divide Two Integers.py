'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        if divisor == 0:
            return 2147483647
        elif divisor == 1:
            result = dividend
        else:
            result = 0
            c, sub = 1, divisor

            while dividend >= divisor:
                if dividend >= sub:
                    dividend -= sub
                    result += c
                    sub <<= 1
                    c <<= 1
                else:
                    sub >>= 1
                    c >>= 1

        if sign:
            result = -result
        return min(max(-2147483648, result), 2147483648)
