class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10:
            n = 10

        count = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ret = 1
        for i in range(n):
            count[i] *= count[i - 1]
            ret += count[i]
        return ret





# 好像是各位数字都要不一样
for i in range(1, 11):
    print(Solution().countNumbersWithUniqueDigits(i))
