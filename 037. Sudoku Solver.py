'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''

from copy import deepcopy

def _pop(board_dict, i, j, target):
    temp = board_dict[i, j]
    if isinstance(temp, int):
        if temp == target:
            return False
    else:
        temp.pop(target, None)
        if len(temp) == 0:
            return False
        elif len(temp) == 1:
            return fill_i_j(board_dict, i, j, next(iter(temp.keys())))
    return True


def fill_i_j(board_dict, i, j, target=None):
    if target is None:
        target = board_dict[i, j]
    else:
        board_dict[i, j] = target

    for k in range(9):
        if j != k and not _pop(board_dict, i, k, target):
            return False
    for k in range(9):
        if i != k and not _pop(board_dict, k, j, target):
            return False
    i0, j0 = i // 3 * 3, j // 3 * 3
    for ii in range(i0, i0 + 3):
        for jj in range(j0, j0 + 3):
            if (ii != i or jj != j) and not _pop(board_dict, ii, jj, target):
                return False
    return True


def init_board(board):
    board_dict = {(i, j): {k + 1: None for k in range(9)}
                  for i in range(9) for j in range(9)}
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                if not fill_i_j(board_dict, i, j, int(board[i][j])):
                    raise Exception('invalid sudoku!')
    return board_dict


def solve(board_dict):
    count = sorted((len(val), key)
                   for key, val in board_dict.items() if isinstance(val, dict))
    if count == []:
        return board_dict
    i, j = count[0][1]
    for elem in board_dict[i, j].copy():
        board_dict2 = deepcopy(board_dict)
        if fill_i_j(board_dict2, i, j, elem):
            result = solve(board_dict2)
            if result:
                return result


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        result = solve(init_board(board))
        for i in range(9):
            for j in range(9):
                board[i][j] = str(result[i, j])


if __name__ == '__main__':
    from pprint import pprint
    import time
    t1 = time.time()
    board = ['8........', '..36.....', '.7..9.2..', '.5...7...', '....457..',
             '...1...3.', '..1....68', '..85...1.', '.9....4..']
    board_dict = init_board(board)
    result = solve(board_dict)

    print()
    for i in range(9):
        for j in range(9):
            print(result[i, j], end='\t')
        print()
    print(time.time() - t1)



    # board = ['.7..16.9.',
    #          '.........',
    #          '.9.73..6.',
    #          '.32.....7',
    #          '9..42.1.3',
    #          '.....1..9',
    #          '3..8.....',
    #          '8.5.97..1',
    #          '7.....58.']
