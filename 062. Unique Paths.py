'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.
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

@memo
def n_choose_k(n, k):
    if k < 0 or k > n:
        return 0
    elif k == 0 or n == k:
        return 1
    else:
        return n_choose_k(n - 1, k - 1) + n_choose_k(n - 1, k)


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return n_choose_k(m + n - 2, m - 1)
