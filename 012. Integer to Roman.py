'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''

roman_unit = [1000, 500, 100, 50, 10, 5, 1]
roman_char = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
roman_sep = [900, 400, 90, 40, 9, 4, 0.1]

def roman_rec(num, u=0):
    for i in range(u, 7):
        if num >= roman_sep[i]:
            if num < roman_unit[i]:
                ii = ((i >> 1) + 1) << 1
                return (roman_char[ii] + roman_char[i] +
                        roman_rec(num + roman_unit[ii] - roman_unit[i], i + 1))
            else:
                return roman_char[i] + roman_rec(num - roman_unit[i], i)
    return ''


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        return roman_rec(num)


if __name__ == '__main__':
    assert Solution().intToRoman(35) == 'XXXV'
    assert Solution().intToRoman(399) == 'CCCXCIX'
    assert Solution().intToRoman(888) == 'DCCCLXXXVIII'
