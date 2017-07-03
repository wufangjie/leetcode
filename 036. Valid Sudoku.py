'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''

def check_part(part):
    exist = {}
    for elem in part:
        if elem != '.':
            if exist.get(elem):
                return False
            exist[elem] = True
    return True


def check(comb):
    for part in comb:
        if not check_part(part):
            return False
    return True


def check_block(board, block_list=range(9)):
    for idx in block_list:
        i, j = idx // 3, idx % 3
        for i in range(3):
            for j in range(3):
                if not check_part(
                        ''.join(board[i * 3 + m][j * 3 + n]
                                for m in range(3) for n in range(3))):
                    return False
    return True


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not check(board):
            return False
        if not check([''.join(part) for part in zip(*board)]):
            return False
        if not check_block(board):
            return False
        return True


if __name__ == '__main__':
    assert Solution().isValidSudoku([
        ".87654321","2........","3........",
        "4........","5........","6........",
        "7........","8........","9........"]) == True
