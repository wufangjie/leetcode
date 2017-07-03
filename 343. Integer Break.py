import math


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n - 1
        if n % 3 == 1:
            return 3 ** ((n - 4) // 3) * 4
        elif n % 3 == 2:
            return 3 ** ((n - 2) // 3) * 2
        else:
            return 3 ** (n // 3)


        # # 事实上, n / math.exp(math.log1p(n) - 1), 可以画简为 e
        # # 注 log1p 是错的, 等价于 log(1 + n), 应改为 log

        # if n == 3:
        #     return 2

        # lof = n / math.exp(math.log1p(n) - 1)
        # if lo == lof:
        #     hi = lo
        # else:
        #     hi = lo + 1

        # theMax = 0
        # for k in range(int(math.ceil((n + 0.) / hi)),
        #                int(math.floor((n + 0.) / lo)) + 1): # python2
        #     if k > 1:
        #         n1 = n - lo * k
        #         theMax = max(theMax, lo ** (k - n1) * (lo + 1) ** n1)
        # return theMax


        # # actually lo == 2
        # kf = math.exp(math.log(n) - 1)
        # k = int(kf) if kf >= 2 else 2

        # lo = n // k
        # n1 = n - lo * k
        # theMax = lo ** (k - n1) * (lo + 1) ** n1

        # if k < kf:
        #     k += 1
        #     lo = n // k
        #     n1 = n - lo * k
        #     theMax = max(theMax, lo ** (k - n1) * (lo + 1) ** n1)
        # return theMax


assert Solution().integerBreak(10) == 36
assert Solution().integerBreak(2) == 1
assert Solution().integerBreak(1) == 0
assert Solution().integerBreak(21) == 2187
assert Solution().integerBreak(3) == 2
assert Solution().integerBreak(30) == 59049
