from functools import reduce


class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ln = len(str(n))
        den = int('1' * ln)
        result = [1 + (k - 1) // den]
        left = (k - 1) % den

        while True:
            if left == 0:
                break
            den //= 10
            result.append((left - 1) // den)
            left = (left - 1) % den

        lr = len(result)
        num = reduce(lambda x, y: 10 * x + y, result)
        num2 = num * 10 ** (ln - lr) - 1 if lr < ln else num
        if num2 > n:
            if lr < ln:
                result = list(map(int, str(num2)))
            den = int('1' * (ln - 1))
            order = (result[0] - 1) * den + 1 + num2 - n + (lr < ln)
            for i in range(1, ln - 1):
                den //= 10
                order += den * result[i] + 1
            return self.findKthNumber(10 ** (ln - 1) - 1, order)
        return num




assert Solution().findKthNumber(13, 2) == 10
assert Solution().findKthNumber(13, 13) == 9
assert Solution().findKthNumber(100, 10) == 17
assert Solution().findKthNumber(7747794, 5857460) == 6271710
assert Solution().findKthNumber(7747794, 7657460) == 918697
assert Solution().findKthNumber(100, 90) == 9
