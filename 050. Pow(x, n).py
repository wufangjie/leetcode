'''
Implement pow(x, n).
'''

from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper._cache = cache
    return wrapper


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        @memo
        def pow_rec(n):
            if n == 1:
                return x
            else:
                temp = n >> 1
                return pow_rec(temp) * pow_rec(n - temp)

        if n == 0:
            return 1
        elif n < 0:
            return 1 / pow_rec(abs(n))
        else:
            return pow_rec(abs(n))


if __name__ == '__main__':
    print(Solution().myPow(8.88023, -1))
