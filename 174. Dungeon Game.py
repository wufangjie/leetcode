class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        nrow, ncol = len(dungeon), len(dungeon[0])
        dp = [float('inf')] * (ncol + 1)
        dp[-2] = 1
        for r in range(nrow-1, -1, -1):
            for c in range(ncol-1, -1, -1):
                dp[c] = max(1, min(dp[c], dp[c+1]) - dungeon[r][c])
        return dp[0]
