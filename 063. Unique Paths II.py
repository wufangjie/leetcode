'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,

There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

The total number of unique paths is 2.

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


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        @memo
        def unique_path_rec(m, n):
            if m < 0 or n < 0:
                return 0
            elif m == 0 and n == 0:
                return 0 if obstacleGrid[0][0] else 1
            else:
                temp = 0
                if obstacleGrid[m][n - 1] == 0:
                    temp += unique_path_rec(m, n - 1)
                if obstacleGrid[m - 1][n] == 0:
                    temp += unique_path_rec(m - 1, n)
                return temp
        if obstacleGrid[-1][-1]:
            return 0
        m, n = len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1
        return unique_path_rec(m, n)


if __name__ == '__main__':
    Solution().uniquePathsWithObstacles([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]])
    Solution().uniquePathsWithObstacles([[0, 1]])
