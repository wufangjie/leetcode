from collections import deque


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # if not matrix: # at least one 0
        #     return matrix
        nrow, ncol = len(matrix), len(matrix[0])
        used = ([[False] * ncol + [True] for _ in range(nrow)]
                + [[True] * (ncol + 1)])

        Q = deque([])
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 0:
                    used[i][j] = True
                    Q.append((i, j))

        while Q:
            i, j = Q.popleft()
            for ii, jj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if not used[ii][jj]:
                    used[ii][jj] = True
                    matrix[ii][jj] = matrix[i][j] + 1
                    Q.append((ii, jj))
        return matrix
