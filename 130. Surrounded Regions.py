from itertools import product, chain

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        nrow, ncol = len(board), len(board[0])
        board_list = [['X'] * ncol for _ in range(nrow)]

        def extend(irow, icol):
            Q = [(irow, icol)] # use stack rather than recursive
            while Q:
                irow, icol = Q.pop()
                for drow in (-1, 1):
                    i = irow + drow
                    if (0 <= i < nrow
                        and board[i][icol] == 'O'
                        and board_list[i][icol] == 'X'):
                        board_list[i][icol] = 'O'
                        Q.append((i, icol))
                for dcol in (-1, 1):
                    j = icol + dcol
                    if (0 <= j < ncol
                        and board[irow][j] == 'O'
                        and board_list[irow][j] == 'X'):
                        board_list[irow][j] = 'O'
                        Q.append((irow, j))

        for irow, icol in chain(product((0, nrow-1), range(ncol)),
                                product(range(nrow), (0, ncol-1))):
                if board[irow][icol] == 'O' and board_list[irow][icol] == 'X':
                    board_list[irow][icol] = 'O'
                    extend(irow, icol)

        for i in range(nrow):
            board[i] = ''.join(board_list[i])
