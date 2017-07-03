import math


class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        # base, n 进制, python2 no math.log2
        n = int(n)
        for l in range(int(math.log(n + 1, 2)), 2, -1):
            mid = int(n ** (1. / (l - 1)))
            if (mid ** l - 1) // (mid - 1) == n:
                return str(mid)
            # NOTE: polynomials expansion
            # (x + 1) ** n > x ** n + x ** (n - 1) + ... + 1
            # so mid - 1 is no way the solution

            # lo, hi = 2, int(n ** (1. / (l - 1))) + 1
            # while lo < hi:
            #     mid = (lo + hi) >> 1
            #     if (mid ** l - 1) // (mid - 1) == n:
            #         return str(mid)
            #     elif (mid ** l - 1) // (mid - 1) > n:
            #         hi = mid - 1
            #     else:
            #         lo = mid + 1
        return str(n - 1)

assert Solution().smallestGoodBase("13") == "3"
assert Solution().smallestGoodBase("4681") == "8"
assert Solution().smallestGoodBase("1000000000000000000") == "999999999999999999"
print(Solution().smallestGoodBase('435356467'))
