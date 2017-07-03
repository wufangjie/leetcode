class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return 'NaN'
        elif numerator == 0:
            return '0'

        sign = (numerator > 0) ^ (denominator > 0)
        num, den = abs(numerator), abs(denominator)
        num_dict = {}

        temp = num // den
        num -= temp * den
        result = [('-' if sign else '') + str(temp) + ('.' if num else '')]

        count = 1
        while num != 0:
            if num in num_dict:
                result.insert(num_dict[num], '(')
                result.append(')')
                break

            num_dict[num] = count
            count += 1
            num *= 10
            temp = num // den
            num -= temp * den
            result.append(str(temp))

        return ''.join(result)


assert Solution().fractionToDecimal(0, 3) == '0'
