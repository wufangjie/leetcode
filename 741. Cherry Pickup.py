class Solution:
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        _inf = float('-inf')
        dp = [[_inf] * (n + 1) for _ in range(m)]
        dp[0][-1] = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    dp[i][j] = _inf
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        if dp[-1][-2] <= 0:
            return max(0, dp[-1][-2])

        dp2 = [dp[0]]
        cache = {}

        def dfs(i1, i2, ij):
            if i1 == i2:
                return dp2[i1][ij - i1]
            if i1 < 0 or i1 > ij or i2 < 0 or i2 > ij:
                return _inf
            if dp[i1][ij - i1] is _inf or dp[i2][ij - i2] is _inf:
                return _inf
            if (i1, i2, ij) in cache:
                return cache[i1, i2, ij]
            if (i2, i1, ij) in cache:
                return cache[i2, i1, ij]

            ret = grid[i1][ij - i1] + grid[i2][ij - i2] + max(
                dfs(i1 - 1, i2 - 1, ij - 1),
                dfs(i1 - 1, i2, ij - 1),
                dfs(i1, i2 - 1, ij - 1),
                dfs(i1, i2, ij - 1))
            cache[i1, i2, ij] = ret
            return ret


        for i in range(1, m):
            dp2.append([dp[i][0]])
            for j in range(1, n):
                if grid[i][j] == -1:
                    dp2[-1].append(_inf)
                else:
                    dp2[-1].append(grid[i][j] + max(
                        dp2[i - 1][j], dp2[i][j - 1], dfs(i - 1, i, i + j - 1)))
        return dp2[-1][n - 1] # not -1






print(Solution().cherryPickup([[0, 1, -1], [1, 0, -1], [1, 1,  1]]), 5)
print(Solution().cherryPickup([[1,1,-1],[1,-1,1],[-1,1,1]]), 0)
print(Solution().cherryPickup([[1,-1,-1,-1,-1],[1,0,1,-1,-1],[0,-1,1,0,1],[1,0,1,1,0],[-1,-1,-1,1,1]]), 10)
print(Solution().cherryPickup([[1,1,1,1,1],[1,1,1,1,1],[1,1,-1,1,1],[0,-1,-1,1,1],[1,1,1,1,1]]), 16)
print(Solution().cherryPickup([[1,1,1,1,1],[1,1,-1,1,1],[-1,-1,1,1,1],[1,1,1,1,1],[-1,1,1,1,1]]), 13)
print(Solution().cherryPickup([[1]]))

a = [[0,0,1,0,0,1,0,1,1,-1,0,0,-1,-1,0,1,1,-1,0,-1],[1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0],[1,0,1,1,0,0,1,0,0,0,1,0,1,1,1,-1,0,1,1,0],[0,1,1,0,0,0,1,0,1,1,0,-1,1,0,0,1,0,0,1,1],[-1,0,-1,1,0,0,1,1,0,0,1,1,0,-1,1,0,0,0,1,1],[0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,1,1,1,0],[0,0,0,1,0,1,1,0,0,1,1,-1,1,0,1,1,0,1,1,0],[0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,1],[0,0,0,-1,1,0,0,1,0,0,1,1,1,1,0,0,0,1,1,0],[1,0,1,1,1,0,0,1,1,0,1,0,0,0,-1,0,-1,0,1,0],[0,1,-1,1,1,1,1,0,1,0,0,1,1,0,-1,1,0,0,-1,0],[0,0,0,0,1,0,1,0,0,-1,0,1,0,-1,0,0,1,0,1,1],[1,-1,-1,0,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,0],[-1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,0,1,0],[0,1,-1,1,1,1,0,0,1,-1,1,1,0,1,0,1,0,-1,1,0],[1,-1,1,0,1,1,1,0,0,0,1,1,1,1,-1,0,0,1,0,-1],[-1,1,0,0,0,1,1,1,1,1,0,1,1,-1,0,1,0,0,1,0],[0,0,0,-1,0,1,0,0,0,0,0,0,1,0,1,1,0,0,0,1],[0,1,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,1],[0,0,0,1,-1,0,-1,1,0,1,0,0,0,0,1,0,0,1,-1,0]]

i = 13
b = [a[j][:i] for j in range(i)]
print(Solution().cherryPickup(a))
#print(b)


# for row in dp2:
#     print(*row, sep='\t')
