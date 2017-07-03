class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        nrow, ncol, theMax = len(matrix), len(matrix[0]), 0
        dp = [[1] * ncol for _ in range(nrow)]
        for v, i, j in sorted([(matrix[i][j], i, j)
                               for i in range(nrow) for j in range(ncol)]):
            for ii, jj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if (0 <= ii < nrow and 0 <= jj < ncol
                    and matrix[i][j] > matrix[ii][jj]):
                        dp[i][j] = max(dp[i][j], dp[ii][jj]+1)
            theMax = max(theMax, dp[i][j])
        return theMax


Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
Solution().longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])
