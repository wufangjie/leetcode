from math import sqrt


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(sqrt(2 * n + 0.25) - 0.5)



print(Solution().arrangeCoins(5))
print(Solution().arrangeCoins(8))
print(Solution().arrangeCoins(1))
print(Solution().arrangeCoins(0))
