'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
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
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        @memo
        def min_path_rec(m, n):
            if m == 0 and n == 0:
                return grid[0][0]
            elif m == 0:
                return min_path_rec(m, n - 1) + grid[m][n]
            elif n == 0:
                return min_path_rec(m - 1, n) + grid[m][n]
            else:
                return min(min_path_rec(m, n - 1),
                           min_path_rec(m - 1, n)) + grid[m][n]
        return min_path_rec(len(grid) - 1, len(grid[0]) - 1)

        # def min_path_rec(m, n):
        #     if m < 0 or n < 0:
        #         return float('inf')
        #     elif m == 0 and n == 0:
        #         return grid[0][0]
        #     else:
        #         return min(min_path_rec(m, n - 1),
        #                    min_path_rec(m - 1, n)) + grid[m][n]
        # return min_path_rec(len(grid) - 1, len(grid[0]) - 1)
