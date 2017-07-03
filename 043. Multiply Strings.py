'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:

    The numbers can be arbitrarily large and are non-negative.
    Converting the input string to integer is NOT allowed.
    You should NOT use internal library such as BigInteger.
'''

# maybe larger block is better

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = len(num1), len(num2)
        result = [0] * (n1 + n2)
        for i1 in range(n1 - 1, -1, -1):
            int_1 = int(num1[i1])
            for i2 in range(n2 - 1, -1, -1):
                result[i1 + i2 + 1] += int_1 * int(num2[i2])

        carry = 0
        for i in range(n1 + n2 - 1, -1, -1):
            result[i] += carry
            carry = result[i] // 10
            result[i] %= 10

        for i, elem in enumerate(result):
            if elem != 0:
                return ''.join(str(x) for x in result[i:])
        return '0'


if __name__ == '__main__':
    assert Solution().multiply('34567', '890') == str(34567 * 890)
    assert Solution().multiply('34567', '1') == '34567'
    assert Solution().multiply('34567', '0') == '0'
