from math import sqrt

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [False, False] + [True] * (n - 2)
        for i in xrange(4, n, 2):
            result[i] = False
        for i in xrange(3, int(sqrt(n)+1), 2):
            if result[i]:
                for i in xrange(i+i, n, i):
                    result[i] = False
        return sum(result)

        # use numpy if possible # python3
        # result = [False, False] + [True] * (n - 2)
        # for i in range(4, n, 2):
        #     result[i] = False
        # for i in range(3, int(sqrt(n)+1), 2):
        #     if result[i]:
        #         for i in range(i+i, n, i):
        #             result[i] = False
        # return sum(result)


if __name__ == '__main__':
    Solution().countPrimes(999983)
