class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        nrow, ncol = len(grid), len(grid[0])
        ret = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    if i == 0 or grid[i - 1][j] == 0:
                        ret += 1
                    if i == nrow - 1 or grid[i + 1][j] == 0:
                        ret += 1
                    if j == 0 or grid[i][j - 1] == 0:
                        ret += 1
                    if j == ncol - 1 or grid[i][j + 1] == 0:
                        ret += 1
        return ret
