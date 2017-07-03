'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        m, n, w = len(board), len(board[0]), len(word)

        def forward(i, j, visited, target):
            result = []
            for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                try:
                    assert ii > -1 and jj > -1
                    if board[ii][jj] == target and (ii, jj) not in visited:
                        result.append((ii, jj))
                except:
                    pass
            return result

        def match_rec(i, j, visited, count):
            if count == w:
                return True
            for i, j in forward(i, j, visited, word[count]):
                if match_rec(i, j, visited.union({(i, j)}), count + 1):
                    return True
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if match_rec(i, j, {(i, j)}, 1):
                        return True
        return False


if __name__ == 'target':
    assert Solution().exist(["ABCE","SFCS","ADEE"], "CCSE")
    assert Solution().exist(["ABCE","SFCS","ADEE"], "CCSEC") == False
    assert Solution().exist(["aa"], "aaa") == False
    assert Solution().exist(["ABCE","SFCS","ADEE"], "ABCB") == False
