class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        nrow, ncol = len(grid), len(grid[0])
        island_dict = {(i, j): 1 for i in range(nrow) for j in range(ncol)
                       if grid[i][j] == '1'}

        def expand(i, j, count):
            for p in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if island_dict.get(p, 0) == 1:
                    island_dict[p] = count
                    expand(p[0], p[1], count)

        count = 2
        for (i, j), v in island_dict.iteritems(): # python2 items is wrong
            if v == 1:
                island_dict[i, j] = count
                expand(i, j, count)
                count += 1
        return count - 2


if __name__ == '__main__':
    assert Solution().numIslands(["11110","11010","11000","00000"]) == 1
    assert Solution().numIslands(["11000", "11000", "00100", "00011"]) == 3
