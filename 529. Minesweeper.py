class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        # board's type is not like testcase
        i0, j0 = click
        if board[i0][j0] == 'M':
            board[i0][j0] = 'X'
            # board[i0] = board[i0][:j0] + 'X' + board[i0][j0+1:]
            return board

        nrow, ncol = len(board), len(board[0])
        # board = [list(row) for row in board]

        def rec(i, j):
            if board[i][j] == 'E':
                board[i][j] = 'B'
                count = 0
                neighbour = []
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        if 0 <= ii < nrow and 0 <= jj < ncol:
                            if board[ii][jj] == 'M':
                                count += 1
                            if count == 0 and board[ii][jj] == 'E':
                                neighbour.append((ii, jj))
                if count:
                    board[i][j] = str(count)
                else:
                    for ii, jj in neighbour:
                        rec(ii, jj)
        rec(i0, j0)
        return board # [''.join(row) for row in board]
