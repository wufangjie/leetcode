'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        backward = 1
        i = len(digits) - 1
        while i >= 0:
            temp = backward + digits[i]
            backward, digits[i] = temp // 10, temp % 10
            if backward == 0:
                break
            i -= 1
        else:
            return [backward] + digits
        return digits

if __name__ == '__main__':
    assert Solution().plusOne([9, 9]) == [1, 0, 0]
