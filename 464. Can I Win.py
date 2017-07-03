# My solution is wrong


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        choosed = maxChoosableInteger
        i, j = 1, maxChoosableInteger - 1
        while choosed < desiredTotal:
            if choosed < desiredTotal <= choosed + i:
                return False
            choosed += i + j
            i += 1
            j -= 1
        return True


assert not Solution().canIWin(10, 40)
# obj = Solution()

# n = 10
# for i in range(1, (n + 1) * n // 2 + 1):
#     print(i, obj.canIWin(n, i))
