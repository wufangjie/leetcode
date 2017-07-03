from functools import reduce


class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a < 10:
            return a
        result = []
        for i in range(9, 1, -1):
            while a % i == 0:
                result.append(i)
                a //= i
        if a > 1:
            return 0
        result = reduce(lambda x, y: 10 * x + y, reversed(result))
        return result if result < 2147483648 else 0
