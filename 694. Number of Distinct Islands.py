class Solution(object):
    def numDistinctIslands(self, grid):
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
                return [0]
            visited[i][j] = 1
            ret = [1]
            for i2, j2 in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                ret.extend(dfs(i2, j2))
            return ret

        types = {(0,)}
        for i in range(nrow):
            for j in range(ncol):
                types.add(tuple(dfs(i, j)))
        return len(types) - 1

print(Solution().numDistinctIslands([[1, 1, 0, 0, 0],
                                     [1, 1, 0, 0, 0],
                                     [0, 0, 0, 1, 1],
                                     [0, 0, 0, 1, 1]]))

print(Solution().numDistinctIslands([[1, 1, 0, 1, 1],
                                     [1, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 1],
                                     [1, 1, 0, 1, 1]]))
