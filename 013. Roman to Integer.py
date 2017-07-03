'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

roman_dict = {
    'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        v_pre = result = 0
        for elem in s:
            v_cur = roman_dict[elem]
            if v_pre != 0:
                if v_cur > v_pre:
                    result += v_cur - v_pre
                    v_pre = 0
                else:
                    result += v_pre
                    v_pre = v_cur
            else:
                v_pre = v_cur
        return result + v_pre


if __name__ == '__main__':
    assert Solution().romanToInt('XXXV') == 35
    assert Solution().romanToInt('CCCXCIX') == 399
    assert Solution().romanToInt('DCCCLXXXVIII') == 888
