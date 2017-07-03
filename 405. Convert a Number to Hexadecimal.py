# list is better than dict
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
       'a', 'b', 'c', 'd', 'e', 'f']


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'

        neg = num < 0
        n = -1 - num if neg else num

        result = []
        while n:
            temp = n & 0b1111
            result.append(lst[15 - temp if neg else temp])
            n >>= 4
        if neg:
            result += ['f'] * (8 - len(result))
        return ''.join(reversed(result))


print(Solution().toHex(-28765))
