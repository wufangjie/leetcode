class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nrow, ncol = len(grid), len(grid[0])
        grid.append([0] * ncol)
        for row in grid:
            row.append(0)
        visited = [[0] * ncol for _ in range(nrow)]

        def dfs(i, j):
            if grid[i][j] == 0 or visited[i][j]:
                return 0
            visited[i][j] = 1
            return 1 + sum(dfs(i2, j2) for i2, j2 in
                           ((i-1, j), (i+1, j), (i, j-1), (i, j+1)))

        theMax = 0
        for i in range(nrow):
            for j in range(ncol):
                temp = dfs(i, j)
                if temp > theMax:
                    theMax = temp
        return theMax


print(Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print(Solution().maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
