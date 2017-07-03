import bisect


cumsum = [(n + 1) * 9 * 10 ** n for n in range(8)]
for i in range(1, len(cumsum)):
    cumsum[i] += cumsum[i - 1]


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n

        i = bisect.bisect_left(cumsum, n)
        n -= cumsum[i - 1] + 1
        num = 10 ** i + n // (i + 1)
        return int(str(num)[n % (i + 1)])


print(Solution().findNthDigit(9998))
assert Solution().findNthDigit(322219) == 5
