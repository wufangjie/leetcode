class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0

        count = 0
        nrow, ncol = len(board), len(board[0])
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == 'X':
                    count += 1 - ((0 if i == 0 else board[i - 1][j] == 'X')
                                  or (0 if j == 0 else board[i][j - 1] == 'X'))
        return count


print(Solution().countBattleships(["X..X","...X","...X"]))
