class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # two bit state 00 01 10 11
        # first bit means last state, second means current state
        if not board:
            return

        def count_neighbor(i, j):
            count = 0
            for ii, jj in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1)):
                if 0 <= ii < m and 0 <= jj < n:
                    count += board[ii][jj] >> 1
            for ii, jj in ((i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
                if 0 <= ii < m and 0 <= jj < n:
                    count += board[ii][jj] & 1
            return count

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                nbs = count_neighbor(i, j)
                board[i][j] &= 1
                if board[i][j]:
                    if 2 <= nbs <= 3:
                        board[i][j] = 3 # 11
                    else:
                        board[i][j] = 2 # 10
                elif nbs == 3:
                    board[i][j] = 1

        for i in range(m):
            for j in range(n):
                board[i][j] &= 1

# import numpy as np
# board = np.random.randint(0, 2, (10, 10)).tolist()
Solution().gameOfLife(board)

# it's not acutally O(1) space (but use integer to carry more informations),
# I hate this
